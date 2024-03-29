from abc import ABC
from typing import List
from src.core.domain.order import Order
from src.core.domain.order_item import OrderItem
from src.core.domain.customer import Customer
from src.core.domain.product import Product
from src.port.usecase.customer_get_usecase import CustomerGetUseCase
from src.core.usecase.customer_get_usecase import CustomerGetUseCaseImpl
from src.port.usecase.order_post_usecase import OrderPostUseCase
from src.port.usecase.product_get_usecase import ProductGetUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.core.usecase.product_get_usecase import ProductGetUseCaseImpl
from src.adapter.spi.persistence.repository.order_repository import OrderRepository
from src.adapter.spi.persistence.mapper.order_mapper import OrderMapper
from src.core.util.logger_custom import Logger

class OrderPostUseCaseImpl(OrderPostUseCase):
    def __init__(self) -> None:
        super().__init__()
        self.__productGetUseCase: ProductGetUseCase = ProductGetUseCaseImpl()
        self.__customerGetUseCase: CustomerGetUseCase = CustomerGetUseCaseImpl()
        self.__repository: Repository = OrderRepository()


    def execute(self, order: Order) -> Order:        
        Logger.info(method=Logger.getMethodCurrent(), message="Start of use case to save order")
        customer: Customer = self.__customerGetUseCase.getByDocumentNumber(order.customerIdentify)
        order.customerName = customer.name        
        order.items = self.__validateItems(order.items)
        order.deliveryAmount = 5.00
        order.calculate()
        self.__repository.save(OrderMapper.parseToModel(order))
        return order

    def __validateItems(self, items: List[OrderItem]): 
        product: Product
        for item in items:
            product : Product = self.__productGetUseCase.getByCode(item.productCode) 
            item.productId = product.id
            item.amount = product.amount
        return items
    