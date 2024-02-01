from typing import List
from src.core.domain.order import Order
from src.adapter.spi.api.schema.base_response import BaseResponse
from src.adapter.spi.api.schema.order_request import OrderRequest
from src.adapter.spi.api.schema.order_response import OrderResponse
from src.adapter.spi.api.mapper.order_item_mapper import OrderItemMapper


class OrderMapper:
    @staticmethod
    def parseToDomain(request: OrderRequest) -> Order:
        return Order(
            customerName = request.customerName,
            customerIdentify = request.customerIdentify,
            items = OrderItemMapper.parseToDomainList(request.items)
        )

    @staticmethod
    def parseToResponse(domain: Order) -> BaseResponse[OrderResponse]:   
        return BaseResponse(
            data = OrderResponse(
                        id = domain.id,
                        issueDateTime = domain.issueDateTime,
                        customerName = domain.customerName,
                        customerIdentify = domain.customerIdentify,
                        deliveryAmount = domain.deliveryAmount,
                        totalAmount = domain.total,                
                        status = domain.status,
                        items = OrderItemMapper.parseToResponseList(domain.items)
                    )
        )
    
    @staticmethod
    def parseToResponseList(domainList: List[Order]) -> BaseResponse[OrderResponse]:
        return BaseResponse(
            data=[OrderMapper.parseToResponse(domain).data for domain in domainList]
        )        
