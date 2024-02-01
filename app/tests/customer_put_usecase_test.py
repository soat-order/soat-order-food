from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.core.usecase.customer_put_usecase import CustomerPutUseCaseImpl
from src.core.domain.customer import Customer
from src.adapter.spi.persistence.model.customer import Customer as CustomerModel
from src.adapter.spi.persistence.repository.customer_repository import CustomerRepository


class CustomerPuttUseCaseTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.useCase : CustomerPutUseCaseImpl = CustomerPutUseCaseImpl()
        self.customerMock: Customer = Customer("NOME TESTE", "11111111112", "teste@email.com.br", "999887766")
        self.customerModelMock: CustomerModel = CustomerModel("NOME TESTE", "11111111111", "teste@email.com.br", "999887766")
    
    @patch.object(CustomerRepository, 'findById')
    @patch.object(CustomerRepository, 'update')
    def test_execute_ok(self, mock_repository_findById, mock_repository_update):
        mock_repository_findById.return_value = MagicMock(self.customerMock)
        mock_repository_update.return_value = MagicMock(self.customerMock)

        result = self.useCase.execute(self.customerMock)
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Customer)
        self.assertEqual(result.name, self.customerMock.name)
