from typing import List
from src.adapter.spi.api.schema.base_response import BaseResponse
from src.adapter.spi.api.schema.product_request import ProductRequest
from src.adapter.spi.api.schema.product_update_request import ProductUpdateRequest
from src.adapter.spi.api.schema.product_response import ProductResponse
from src.core.domain.product import Product


class ProductMapper:
    @staticmethod
    def parseToDomain(request: ProductRequest) -> Product:
        return Product(code=request.code, name=request.name,
                                    amount=request.amount, type=request.type)

    @staticmethod
    def parseUpdateToDomain(request: ProductUpdateRequest) -> Product:
        product = Product(code=None, name=request.name,
                                    amount=request.amount, type=request.type)
        product.id = request.id
        return product

    @staticmethod
    def parseToResponse(domain: Product) -> BaseResponse:
        return BaseResponse(data=ProductResponse(id=domain.id, code=domain.code, name=domain.name,
                                    amount=domain.amount, type=domain.type))
    
    @staticmethod
    def parseToResponseList(domainList: List[Product]) -> BaseResponse[ProductResponse]:
        return BaseResponse(data=[ProductMapper.parseToResponse(domain).data for domain in domainList])        
