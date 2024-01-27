from abc import ABC
from src.core.domain.product import Product


class ProductPostUseCase(ABC):
    def execute(self, product: Product) -> Product:
        raise NotImplementedError
