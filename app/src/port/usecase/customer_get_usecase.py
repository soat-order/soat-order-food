from abc import abstractmethod, ABC
from typing import List
from src.core.domain.customer import Customer


class CustomerGetUseCase(ABC):
    @abstractmethod
    def getById(self, id: str) -> Customer:
        raise NotImplementedError

    @abstractmethod
    def getByDocumentNumber(self, documentNumber: str) -> Customer:
        raise NotImplementedError

    @abstractmethod
    def getByAll(self) -> List[Customer]:
        raise NotImplementedError
    