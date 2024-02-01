from typing import List
from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.core.usecase.customer_get_usecase import CustomerGetUseCaseImpl
from src.core.domain.customer import Customer
from src.adapter.spi.persistence.model.customer import Customer as CustomerModel
from src.adapter.spi.persistence.repository.customer_repository import CustomerRepository


class CustomerGetUseCaseTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.useCase : CustomerGetUseCaseImpl = CustomerGetUseCaseImpl()
        self.customerMock: Customer = Customer("NOME TESTE", "11111111111", "teste@email.com.br", "999887766")
        self.customerModelMock: CustomerModel = CustomerModel("NOME TESTE", "11111111111", "teste@email.com.br", "999887766")

    @patch.object(CustomerRepository, 'findById')
    def test_findById_ok(self, mock_repository_findById):
        mock_repository_findById.return_value = self.customerModelMock        
        result = self.useCase.getById("1")
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Customer)
        self.assertEqual(result.documentNumber, self.customerMock.documentNumber)

    @patch.object(CustomerRepository, 'findByAll')
    def test_getByAll_ok(self, mock_repository_findByAll):
        mock_repository_findByAll.return_value = [self.customerModelMock]        
        result = self.useCase.getByAll()
        self.assertIsNotNone(result)
        # self.assertEqual(type(result), List[Customer])
        self.assertEqual(result[0].documentNumber, self.customerMock.documentNumber)


    @patch.object(CustomerRepository, 'findByDocumentNumber')
    def test_getByDocumentNumber_ok(self, mock_repository_findByDocumentNumber):
        mock_repository_findByDocumentNumber.return_value = self.customerModelMock        
        result = self.useCase.getByDocumentNumber(self.customerMock.documentNumber)
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Customer)
        self.assertEqual(result.documentNumber, self.customerMock.documentNumber)
