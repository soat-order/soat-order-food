from typing import List
from src.core.util.logger_custom import Logger
from src.core.exception.business_exception import BusinessException
from src.adapter.spi.persistence.model.product import Product
from src.adapter.spi.persistence.repository.repository_default import RepositoryDefault
from src.adapter.spi.persistence.mapper.product_mapper import ProductMapper


class ProductRepository(RepositoryDefault[Product, str]):
    def __init__(self) -> None:
        super().__init__(Product)

    def findByCode(self, code: str) -> Product:
        try:
            Logger.info(Logger.getClassMethodCurrent(), f"Start search by code: {code}")        
            return self.parseToModel(self._getSession().find_one({"code": code}))
        except Exception as ex:
            raise BusinessException(status_code=404,
                            detail=f"Not found product by code :{code}")

    def parseToModel(self, dict: dict) -> Product:
        return ProductMapper.parseDictToModel(dict)
