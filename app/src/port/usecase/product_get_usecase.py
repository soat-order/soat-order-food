from typing import List
from abc import ABC, abstractclassmethod
from src.core.domain.product import Product
from src.core.domain.enum.producty_type_enum import ProductType


class ProductGetUseCase(ABC):
    @abstractclassmethod
    def getById(self, id: str) -> Product:
        raise NotImplementedError

    @abstractclassmethod
    def getByCode(self, code: str) -> Product:
        raise NotImplementedError

    # def getByType(self, type: ProductType) -> Product:
    #     raise NotImplementedError

    # def getByDescribe(self, type: ProductType) -> Product:
    #     raise NotImplementedError
    
    @abstractclassmethod
    def getByAll(self) -> List[Product]:
        raise NotImplementedError