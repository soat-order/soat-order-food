from fastapi import APIRouter, status, Path
from src.port.usecase.product_post_usecase import ProductPostUseCase
from src.port.usecase.product_put_usecase import ProductPutUseCase
from src.core.usecase.product_post_usecase import ProductPostUseCaseImpl
from src.core.usecase.product_put_usecase import ProductPutUseCaseImpl
from src.port.usecase.product_get_usecase import ProductGetUseCase
from src.core.usecase.product_get_usecase import ProductGetUseCaseImpl
from src.core.domain.enum.producty_type_enum import ProductType
from src.adapter.spi.api.validator.validator import Validator
from src.adapter.spi.api.mapper.product_mapper import ProductMapper
from src.adapter.spi.api.schema.product_request import ProductRequest
from src.adapter.spi.api.schema.base_response import BaseResponse
from src.adapter.spi.api.schema.product_update_request import ProductUpdateRequest


router = APIRouter()
__productPostUseCase: ProductPostUseCase = ProductPostUseCaseImpl()
__productPutUseCase: ProductPutUseCase = ProductPutUseCaseImpl()
__productGetUseCase: ProductGetUseCase = ProductGetUseCaseImpl()

validator: Validator = Validator()

@router.post(path='/', status_code=status.HTTP_201_CREATED)
async def save(product: ProductRequest):
    validator.validateProduct(product)
    __productPostUseCase.execute(ProductMapper.parseToDomain(product))    

@router.put(path='/', status_code=status.HTTP_204_NO_CONTENT)
async def update(product: ProductUpdateRequest):
    validator.validateProductUpdate(product)
    __productPutUseCase.execute(ProductMapper.parseUpdateToDomain(product))    

@router.get(path='/{id}', status_code=status.HTTP_200_OK, response_model=BaseResponse)
async def getById(id: str):
    return ProductMapper.parseToResponse(__productGetUseCase.getById(id))

@router.get(path='/code/{code}', status_code=status.HTTP_200_OK)
async def getByCode(code: str = Path(..., title="Valid code", regex="[A-Z0-9]{4,30}")):
    return ProductMapper.parseToResponse(__productGetUseCase.getByCode(code))

@router.get(path='/category/{category}', status_code=status.HTTP_200_OK)
async def getByCategory(category: str = Path(..., title="Valid product category")):
    validator.validateEnum(ProductType, "category", category)
    return ProductMapper.parseToResponseList(__productGetUseCase.getByType(category))

@router.get(path='/', status_code=status.HTTP_200_OK)
async def getByAll():
    return ProductMapper.parseToResponseList(__productGetUseCase.getByAll())

