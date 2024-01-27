from abc import abstractmethod, ABC
from src.core.domain.product import Product


class ProductPutUseCase(ABC):
    @abstractmethod
    def execute(self, product: Product) -> Product:
        pass    