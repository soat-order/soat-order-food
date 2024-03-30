from typing import List
from src.core.domain.customer import Customer
from src.core.util.string_util import StringUtil
from src.port.usecase.customer_get_usecase import CustomerGetUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.adapter.spi.persistence.repository.customer_repository import CustomerRepository
from src.adapter.spi.persistence.mapper.customer_mapper import CustomerMapper

respository: Repository = CustomerRepository()

class CustomerGetUseCaseImpl(CustomerGetUseCase):
    def getById(self, id: str) -> Customer:
        return CustomerMapper.parseToDomain(respository.findById(id))
    
    def getByDocumentNumber(self, documentNumber: str) -> Customer:
        return CustomerMapper.parseToDomain(respository.findByDocumentNumber(StringUtil.formatDocumentNumber(documentNumber)))
       
    def getByAll(self) -> List[Customer]:
        return respository.findByAll()