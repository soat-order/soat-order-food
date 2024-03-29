from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.core.usecase.order_put_usecase import OrderPutUseCaseImpl
from src.core.domain.order import Order
from src.core.domain.order import OrderItem
from src.core.domain.enum.order_status_enum import OrderStatusEnum
from src.adapter.spi.persistence.model.order import Order as OrderModel
from src.adapter.spi.persistence.model.order_item import OrderItem as OrderItemModel
from src.adapter.spi.persistence.repository.order_repository import OrderRepository
from datetime import datetime


class OrderPuttUseCaseTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.useCase : OrderPutUseCaseImpl = OrderPutUseCaseImpl()
        self.orderItemMock: OrderItem = OrderItem(productCode="1", quantity=1.0, amount=1.0, note="TESTE")
        self.orderItemModelMock: OrderItemModel = OrderItemModel(productId="1", quantity=1.0, amount=1.0, note="TESTE")
        self.orderMock: Order = Order(customerName="NOME TESTE",customerIdentify="11111111112", items=[self.orderItemMock],  status=OrderStatusEnum.IN_PREPARATION)
        self.orderModelMock: OrderModel = OrderModel(customerName="NOME TESTE",customerIdentify="11111111112", items=[self.orderItemModelMock],  status=OrderStatusEnum.IN_PREPARATION.name, deliveryAmount=5.00, totalAmount=10.0)
    
    @patch.object(OrderRepository, 'findById')
    @patch.object(OrderRepository, 'updateStatus')
    def test_execute_ok(self, mock_repository_findById, mock_repository_update):
        mock_repository_findById.return_value = self.orderModelMock
        # mock_repository_update.return_value = self.orderMock
        mock_repository_update.return_value = self.orderModelMock

        result = self.useCase.updateStatus(id="1", status=OrderStatusEnum.READY)
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Order)
        self.assertEqual(result.customerName, self.orderMock.customerName)
