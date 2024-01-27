from typing import List, Any
from src.core.domain.customer import Customer
from src.core.domain.enum.producty_type_enum import ProductType 
from src.adapter.spi.persistence.model.customer import Customer as CustomerModel

class CustomerMapper:
    @staticmethod
    def parseToModel(domain: Customer) -> CustomerModel:
        model = CustomerModel(name=domain.name, documentNumber=domain.documentNumber, 
                    email=domain.email, phoneNumber=domain.phoneNumber)
        if (domain.id != None):
            model.id = domain.id
        return model
    
    @staticmethod
    def parseToDomain(model: Customer) -> Customer:
        domain = Customer(name=model.name, documentNumber=model.documentNumber,
                    email=model.email, phoneNumber=model.phoneNumber)
        domain.id = model.id
        return domain
        
    @staticmethod
    def parseToDomainList(modelList: List[CustomerModel]) -> List[Customer]:
        return [CustomerMapper.parseToDomain(model) for model in modelList]

    @staticmethod
    def parseDictToModel(dictModel) -> Any:
        # devido ao findAll retornar um CURSOR neste caso precisa chamar o metodo parseDictToModelList
        if (not isinstance(dictModel, dict)):
            return CustomerMapper.parseDictToModelList(dictModel)        

        customer = CustomerModel(name=dictModel['name'], documentNumber=dictModel['documentNumber'], 
                    email=dictModel['email'], phoneNumber=dictModel['phoneNumber'])
        customer.id = dictModel['_id']
        return customer

    @staticmethod
    def parseDictToModelList(dictList: List[dict]) -> List[CustomerModel]:
        return list(CustomerMapper.parseDictToModel(dict) for dict in dictList)
