from src.core.domain.order import Order
from src.core.domain.enum.order_status_enum import OrderStatusEnum
from src.port.usecase.order_put_usecase import OrderPutUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.adapter.spi.persistence.repository.order_repository import OrderRepository
from src.adapter.spi.persistence.mapper.order_mapper import OrderMapper
from src.core.util.logger_custom import Logger


class OrderPutUseCaseImpl(OrderPutUseCase):
    def __init__(self) -> None:
        self.__respository: Repository = OrderRepository()
        
    def updateStatus(self, id: str, status: OrderStatusEnum) -> Order:
        order: Order = self.__findById(id)
        order.status = status
        self.__respository.updateStatus(OrderMapper.parseToModel(order))
        return order


    def __findById(self, id: str) -> Order:
        return OrderMapper.parseToDomain(self.__respository.findById(id))
    
    # def __toUpdate(self, productUpdate: Product, product: Product) -> Product:
    #     product.name = productUpdate.name if(not StringUtil.isEmpty(productUpdate.name)) else product.name
    #     product.amount = productUpdate.amount if(not StringUtil.isEmpty(productUpdate.amount)) else product.amount
    #     product.type = productUpdate.type if(not StringUtil.isEmpty(productUpdate.type)) else product.type.value
    #     return product
