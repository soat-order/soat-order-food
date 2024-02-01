from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.core.usecase.customer_post_usecase import CustomerPostUseCaseImpl
from src.core.domain.customer import Customer
from src.adapter.spi.persistence.model.customer import Customer as CustomerModel
from src.adapter.spi.persistence.repository.customer_repository import CustomerRepository


class CustomerPostUseCaseTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.useCase : CustomerPostUseCaseImpl = CustomerPostUseCaseImpl()
        self.customerMock: Customer = Customer("NOME TESTE", "11111111112", "teste@email.com.br", "999887766")
        self.customerModelMock: CustomerModel = CustomerModel("NOME TESTE", "11111111111", "teste@email.com.br", "999887766")
    
    @patch.object(CustomerRepository, 'save')
    def test_saveCustomer_ok(self, mock_repository):
        mock_repository.return_value = MagicMock(self.customerModelMock)
        result = self.useCase.execute(self.customerMock)
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Customer)
        self.assertEqual(result.name, "NOME TESTE")
