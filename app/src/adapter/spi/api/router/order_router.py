from fastapi import APIRouter, status, Path
from src.core.domain.enum.order_status_enum import OrderStatusEnum
from src.port.usecase.order_post_usecase import OrderPostUseCase
from src.port.usecase.order_put_usecase import OrderPutUseCase
from src.port.usecase.order_get_usecase import OrderGetUseCase
from src.core.usecase.order_post_usecase import OrderPostUseCaseImpl
from src.core.usecase.order_put_usecase import OrderPutUseCaseImpl
from src.core.usecase.order_get_usecase import OrderGetUseCaseImpl
from src.adapter.spi.api.schema.order_request import OrderRequest
from src.adapter.spi.api.validator.validator import Validator
from src.adapter.spi.api.mapper.order_mapper import OrderMapper
from src.config.settings_config import settings

router = APIRouter()
__orderPostUseCase: OrderPostUseCase = OrderPostUseCaseImpl()
__orderPutUseCase: OrderPutUseCase = OrderPutUseCaseImpl()
__orderGetUseCase: OrderGetUseCase = OrderGetUseCaseImpl()

validator: Validator = Validator()

@router.post(path='/', status_code=status.HTTP_201_CREATED)
async def save(order: OrderRequest):
    validator.validateOrder(order)
    __orderPostUseCase.execute(OrderMapper.parseToDomain(order))    

@router.put(path='/{id}/status/{status}', status_code=status.HTTP_204_NO_CONTENT)
async def updateStatus(id: str, status: str):
    validator.validateEnum(OrderStatusEnum, "status", status)
    __orderPutUseCase.updateStatus(id, OrderStatusEnum.valueOf(status))

@router.get(path='/{id}', status_code=status.HTTP_200_OK)
async def getById(id: str):
    return OrderMapper.parseToResponse(__orderGetUseCase.getById(id))    

# @router.get(path='/document/{documentNumber}/status/', status_code=status.HTTP_200_OK)
# async def getByDocumentNumber(documentNumber: str = Path(..., title="Valid document number", regex="([0-9]{11})|([0-9]{14})"), x: str):    
#     return OrderMapper.parseToResponse(__orderGetUseCase.getByStatus(documentNumber))    

@router.get(path='/status/pending', status_code=status.HTTP_200_OK)
async def getByOrderPending():    
    return OrderMapper.parseToResponseList(__orderGetUseCase.getByOrderPending())    

@router.get(path='/', status_code=status.HTTP_200_OK)
async def getAll():
    return OrderMapper.parseToResponseList(__orderGetUseCase.getByAll())
