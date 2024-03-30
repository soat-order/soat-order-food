from typing import Any
from src.adapter.spi.persistence.repository.repository_default import RepositoryDefault
from src.adapter.spi.persistence.model.customer import Customer
from src.adapter.spi.persistence.mapper.customer_mapper import CustomerMapper
from src.core.exception.business_exception import BusinessException


class CustomerRepository(RepositoryDefault[Customer, int]):
    def __init__(self) -> None:
        super().__init__(Customer)        

    def findByDocumentNumber(self, documentNumber: str) -> Customer:
        try:
            customer: Customer = self.parseToModel(self._getSession().find_one({"documentNumber": documentNumber}))
            if (customer.inactive == False):
                return customer
            else:
                raise BusinessException(status_code=400,
                            detail=f"Not found {self.modelType.__name__} by documentNumber :{documentNumber}")        
        except Exception as ex:            
            raise BusinessException(status_code=404,
                            detail=f"Not found {self.modelType.__name__} by documentNumber :{documentNumber}")        

    def parseToModel(self, dict: dict) -> Customer:
        return CustomerMapper.parseDictToModel(dict)
