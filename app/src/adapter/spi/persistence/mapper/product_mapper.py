from typing import List, Any
from src.core.domain.product import Product
from src.core.domain.enum.producty_type_enum import ProductType 
from src.adapter.spi.persistence.model.product import Product as ProductModel

class ProductMapper:
    @staticmethod
    def parseToModel(domain: Product) -> ProductModel:
        model = ProductModel(domain.code, name=domain.name, 
                    amount=domain.amount, type=domain.type)
        if (domain.id != None):
            model.id = domain.id
        return model

    
    @staticmethod
    def parseToDomain(model: ProductModel) -> Product:
        domain = Product(code=model.code, name=model.name,
                    amount=model.amount, type=ProductType(model.type))
        domain.id = model.id
        return domain
        
    @staticmethod
    def parseToDomainList(modelList: List[ProductModel]) -> List[Product]:
        return [ProductMapper.parseToDomain(model) for model in modelList]

    @staticmethod
    def parseDictToModel(dictModel) -> Any:
        # devido ao findAll retornar um CURSOR neste caso precisa chamar o metodo parseDictToModelList
        if (not isinstance(dictModel, dict)):
            return ProductMapper.parseDictToModelList(dictModel)
        
        product = ProductModel(code=dictModel['code'], name=dictModel['name'], 
                    amount=dictModel['amount'], type=dictModel['type'])
        product.id = dictModel['_id']
        return product

    @staticmethod
    def parseDictToModelList(dictList: List[dict]) -> List[ProductModel]:
        return list(ProductMapper.parseDictToModel(dict) for dict in dictList)
