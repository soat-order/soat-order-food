from typing import List
from src.core.domain.product import Product
from src.core.domain.enum.producty_type_enum import ProductType
from src.port.usecase.product_get_usecase import ProductGetUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.adapter.spi.persistence.repository.product_repository import ProductRepository
from src.adapter.spi.persistence.mapper.product_mapper import ProductMapper
from src.core.util.logger_custom import Logger

respository: Repository = ProductRepository()

class ProductGetUseCaseImpl(ProductGetUseCase):

    def getById(self, id: str) -> Product:
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case to search id: {id}")
        return ProductMapper.parseToDomain(respository.findById(id))

    def getByCode(self, code: str) -> Product:
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case to search code: {code}")
        return ProductMapper.parseToDomain(respository.findByCode(code))

    def getByType(self, type: str) -> List[Product]:        
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case to search product type: {type}")
        return ProductMapper.parseToDomainList(respository.findByFilter({'type': ProductType.valueOf(type).value}))

    def getByAll(self) -> List[Product]:
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case to search all")
        return ProductMapper.parseToDomainList(respository.findByAll())
