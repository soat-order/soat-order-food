from typing import List
from src.core.domain.order import Order
from src.core.domain.order_item import OrderItem
from src.core.domain.product import Product
from src.core.domain.enum.order_status_enum import OrderStatusEnum
from src.port.usecase.order_get_usecase import OrderGetUseCase
from src.port.usecase.product_get_usecase import ProductGetUseCase
from src.port.usecase.payment_get_usecase import PaymentGetUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.core.usecase.product_get_usecase import ProductGetUseCaseImpl
from src.core.usecase.payment_get_usecase import PaymentGetUseCaseImpl
from src.adapter.spi.persistence.repository.order_repository import OrderRepository
from src.adapter.spi.persistence.mapper.order_mapper import OrderMapper
from src.core.util.string_util import StringUtil
from src.core.util.logger_custom import Logger


class OrderGetUseCaseImpl(OrderGetUseCase):
    def __init__(self):
        self.__respository: Repository = OrderRepository()
        self.__productGetUseCase: ProductGetUseCase = ProductGetUseCaseImpl()
        self.__paymentGetUseCase: PaymentGetUseCase = PaymentGetUseCaseImpl()

    def getById(self, id: str) -> Order:
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case to search order by id: {id}")
        order: Order = OrderMapper.parseToDomain(self.__respository.findById(id))
        order.items = self.__getByOrderItemProduct(order.items)
        order.payments = self.__paymentGetUseCase.getByOrderId(orderId=order.id)
        return order
        
    def getByCustomerAndStatus(self, documentNumber: str, status: str) -> List[Order]:
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case to search order by customer: {documentNumber} and status: {status}")
        orderList = OrderMapper.parseToDomainList(self.__respository.findByFilter({'customerIdentify': StringUtil.formatDocumentNumber(documentNumber), 'status': OrderStatusEnum.valueOf(status).value}))
        orderList.sort(key=lambda order: order.issueDateTime, reverse=True)        
        return orderList
       
    def getByOrderPending(self) -> List[Order]:
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case to search order peding")
        orderList: List[Order] = OrderMapper.parseToDomainList(self.__respository.findByFilter({'status': {'$ne': OrderStatusEnum.FINISHED.value}}))
        orderList.sort(key=lambda order: order.issueDateTime, reverse=True)        
        return orderList

    def getByAll(self) -> List[Order]:
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case to search all orders")
        orderList: List[Order] = OrderMapper.parseToDomainList(self.__respository.findByAll())
        for order in orderList:
            order.items = self.__getByOrderItemProduct(order.items)
        return orderList
    
    def __getByOrderItemProduct(self,items: List[OrderItem]) -> List[OrderItem]:
        product: Product
        for item in items:
            product = self.__productGetUseCase.getById(item.productId) 
            item.productCode = product.code
            item.productName = product.name
        return items