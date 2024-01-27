from src.core.domain.product import Product
from src.port.usecase.product_post_usecase import ProductPostUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.adapter.spi.persistence.repository.product_repository import ProductRepository
from src.adapter.spi.persistence.mapper.product_mapper import ProductMapper
from src.core.util.logger_custom import Logger

respository: Repository = ProductRepository()

class ProductPostUseCaseImpl(ProductPostUseCase):
    def execute(self, product: Product) -> Product:
        Logger.info(method=Logger.getMethodCurrent(), message="Start of use case to save")
        respository.save(ProductMapper.parseToModel(product))
        return product
