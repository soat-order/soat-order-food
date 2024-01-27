from abc import ABC
from src.core.domain.product import Product


class ProductPutUseCase(ABC):
    def execute(self, product: Product) -> Product:
        raise NotImplementedError

class ProductDeleteUseCase(ABC):
    def execute(self, id: int) -> Product:
        raise NotImplementedError
