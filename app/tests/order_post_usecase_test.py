from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.core.usecase.order_post_usecase import OrderPostUseCaseImpl
from src.core.usecase.product_get_usecase import ProductGetUseCaseImpl
from src.core.usecase.customer_get_usecase import CustomerGetUseCaseImpl
from src.core.domain.customer import Customer
from src.core.domain.product import Product
from src.core.domain.order import Order
from src.core.domain.order import OrderItem
from src.core.domain.enum.order_status_enum import OrderStatusEnum
from src.core.domain.enum.producty_type_enum import ProductType
from src.adapter.spi.persistence.model.order import Order as OrderModel
from src.adapter.spi.persistence.model.order_item import OrderItem as OrderItemModel
from src.adapter.spi.persistence.repository.order_repository import OrderRepository
from datetime import datetime


class OrderPostUseCaseTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        print("================orderm=============init===================")
        self.useCase : OrderPostUseCaseImpl = OrderPostUseCaseImpl()
        self.orderItemMock: OrderItem = OrderItem(productCode="1", quantity=1.0, amount=1.0, note="TESTE")
        self.orderItemModelMock: OrderItemModel = OrderItemModel(productId="1", quantity=1.0, amount=1.0, note="TESTE")
        self.orderMock: Order = Order(customerName="NOME TESTE",customerIdentify="11111111112", items=[self.orderItemMock],  status=OrderStatusEnum.IN_PREPARATION)
        self.orderModelMock: OrderModel = OrderModel(customerName="NOME TESTE",customerIdentify="11111111112", items=[self.orderItemModelMock],  status=OrderStatusEnum.IN_PREPARATION.name, deliveryAmount=5.00, totalAmount=10.0)
        self.customerMock: Customer = Customer("NOME TESTE", "11111111111", "teste@email.com.br", "999887766")
        self.productMock: Product = Product(code="1",name="PRODUTO TESTE", amount=5.0, type=ProductType.BEVERAGE)
        
    
    @patch.object(ProductGetUseCaseImpl, 'getByCode')
    @patch.object(CustomerGetUseCaseImpl, 'getByDocumentNumber')
    @patch.object(OrderRepository, 'save')
    def test_execute_ok(self, mock_repository_save, mock_repository_getByDocumentNumber, mock_repository_getByCode):
        mock_repository_getByCode.return_value = MagicMock(self.productMock)
        mock_repository_getByDocumentNumber.return_value = self.customerMock
        mock_repository_save.return_value = self.orderModelMock

        result = self.useCase.execute(self.orderMock)
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Order)
        self.assertEqual(result.customerName, self.orderMock.customerName)
