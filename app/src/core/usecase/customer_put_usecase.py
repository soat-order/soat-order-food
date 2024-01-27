from src.core.domain.customer import Customer
from src.port.usecase.customer_put_usecase import CustomerPutUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.adapter.spi.persistence.repository.customer_repository import CustomerRepository
from src.adapter.spi.persistence.mapper.customer_mapper import CustomerMapper
from src.core.util.string_util import StringUtil
from src.core.util.logger_custom import Logger

respository: Repository = CustomerRepository()

class CustomerPutUseCaseImpl(CustomerPutUseCase):
    def execute(self, customerUpdate: Customer) -> Customer:
        Logger.info(method=Logger.getMethodCurrent(), message="Start of use case to update")
        customer : Customer = CustomerMapper.parseToDomain(self.__findById(customerUpdate.id))
        customer = self.__toUpdate(customerUpdate, customer)
        respository.update(CustomerMapper.parseToModel(customer))
        return customer

    def __findById(self, id: str) -> Customer:
        return respository.findById(id)
    
    def __toUpdate(self, customerUpdate: Customer, customer: Customer) -> Customer:
        customer.name = customerUpdate.name if (not StringUtil.isEmpty(customerUpdate.name)) else customer.name
        customer.email = customerUpdate.email if (not StringUtil.isEmpty(customerUpdate.email)) else customer.email
        customer.phoneNumber = customerUpdate.phoneNumber if (not StringUtil.isEmpty(customerUpdate.phoneNumber)) else customer.phoneNumber
        return customer
