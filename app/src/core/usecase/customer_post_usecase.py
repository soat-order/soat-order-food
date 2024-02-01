from src.core.domain.customer import Customer
from src.port.usecase.customer_post_usecase import CustomerPostUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.adapter.spi.persistence.repository.customer_repository import CustomerRepository
from src.adapter.spi.persistence.mapper.customer_mapper import CustomerMapper
from src.core.util.logger_custom import Logger


class CustomerPostUseCaseImpl(CustomerPostUseCase):
    def __init__(self) -> None:
        super().__init__()
        self.__repository: Repository = CustomerRepository()


    def execute(self, customer: Customer) -> Customer:
        Logger.info(method=Logger.getMethodCurrent(), message="Start of use case to save")
        self.__repository.save(CustomerMapper.parseToModel(customer))
        return customer
