from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from src.adapter.spi.api.schema.order_item_response import OrderItemResponse
from src.adapter.spi.api.schema.payment_response import PaymentResponse


@dataclass
class OrderResponse:
    id: str
    issueDateTime: datetime
    customerName: str
    customerIdentify: str
    deliveryAmount: float
    totalAmount: float
    status: str
    items: List[OrderItemResponse] = field(default_factory=List[OrderItemResponse])
    payments: List[PaymentResponse] = field(default_factory=List[PaymentResponse])
