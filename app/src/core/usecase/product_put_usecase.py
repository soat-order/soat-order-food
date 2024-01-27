from src.core.domain.product import Product
from src.port.usecase.product_put_usecase import ProductPutUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.adapter.spi.persistence.repository.product_repository import ProductRepository
from src.adapter.spi.persistence.mapper.product_mapper import ProductMapper
from src.core.util.string_util import StringUtil
from src.core.util.logger_custom import Logger

respository: Repository = ProductRepository()

class ProductPutUseCaseImpl(ProductPutUseCase):
    def execute(self, productUpdate: Product) -> Product:
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case to update: {productUpdate.id}")
        product : Product = ProductMapper.parseToDomain(self.__findById(productUpdate.id))
        product = self.__toUpdate(productUpdate, product)
        respository.update(ProductMapper.parseToModel(product))
        return product

    def __findById(self, id: str) -> Product:
        return respository.findById(id)
    
    def __toUpdate(self, productUpdate: Product, product: Product) -> Product:
        product.name = productUpdate.name if(not StringUtil.isEmpty(productUpdate.name)) else product.name
        product.amount = productUpdate.amount if(not StringUtil.isEmpty(productUpdate.amount)) else product.amount
        product.type = productUpdate.type if(not StringUtil.isEmpty(productUpdate.type)) else product.type.value
        return product
