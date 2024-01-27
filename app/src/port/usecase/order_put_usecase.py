from abc import abstractmethod, ABC
from src.core.domain.order import Order
from src.core.domain.enum.order_status_enum import OrderStatusEnum


class OrderPutUseCase(ABC):
    @abstractmethod
    def updateStatus(self, status: OrderStatusEnum) -> Order:
        pass    