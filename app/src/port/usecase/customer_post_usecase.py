from abc import abstractmethod, ABC
from typing import List
from src.core.domain.customer import Customer


class CustomerPostUseCase(ABC):
    @abstractmethod
    def execute(self, customer: Customer) -> Customer:
        raise NotImplementedError
