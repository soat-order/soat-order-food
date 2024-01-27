from abc import abstractmethod, ABC
from typing import List
from src.core.domain.order import Order


class OrderGetUseCase(ABC):
    @abstractmethod
    def getById(self, id: str) -> Order:
        raise NotImplementedError

    @abstractmethod
    def getByCustomerAndStatus(self, documentNumber: str, status: str) -> List[Order]:
        raise NotImplementedError

    @abstractmethod
    def getByOrderPending(self) -> List[Order]:
        raise NotImplementedError

    @abstractmethod
    def getByAll(self) -> List[Order]:
        raise NotImplementedError
    