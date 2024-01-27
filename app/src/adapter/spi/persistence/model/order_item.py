import uuid
from dataclasses import dataclass, field
from decimal import *

@dataclass
class OrderItem:
    # orderId: str = field(init=False, default=None)
    productId: str = field(default=None)
    quantity: float = field(default=None)
    amount: float = field(default=None)
    note: str = field(default=None)

    @property
    def total(self):
        return (self.amount * self.quantity)