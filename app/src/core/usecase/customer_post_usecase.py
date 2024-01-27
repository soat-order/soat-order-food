from src.core.domain.customer import Customer
from src.port.usecase.customer_post_usecase import CustomerPostUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.adapter.spi.persistence.repository.customer_repository import CustomerRepository
from src.adapter.spi.persistence.mapper.customer_mapper import CustomerMapper
from src.core.util.logger_custom import Logger

respository: Repository = CustomerRepository()

class CustomerPostUseCaseImpl(CustomerPostUseCase):
    def execute(self, customer: Customer) -> Customer:
        Logger.info(method=Logger.getMethodCurrent(), message="Start of use case to save")
        respository.save(CustomerMapper.parseToModel(customer))
        return customer
