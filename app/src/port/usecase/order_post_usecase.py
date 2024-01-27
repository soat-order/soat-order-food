from abc import ABC
from src.core.domain.order import Order


class OrderPostUseCase(ABC):
    def execute(self, order: Order) -> Order:
        raise NotImplementedError
