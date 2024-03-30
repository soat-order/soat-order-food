from abc import abstractmethod, ABC
from src.core.domain.customer import Customer


class CustomerPutUseCase(ABC):
    @abstractmethod
    def execute(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def inactive(self, id: str, inactive: bool) -> Customer:
        pass    