from typing import List
from datetime import datetime
from dataclasses import dataclass, field
from decimal import *
from src.core.domain.order_item import OrderItem
from src.core.domain.payment import Payment
from src.core.domain.enum.order_status_enum import OrderStatusEnum
# from src.core.domain.address import Address


@dataclass
class Order():
    id: str = field(init=False, default=None)
    issueDateTime: datetime = field(init=False)
    customerName: str = field(default=None)
    customerIdentify: str = field(default=None)
    deliveryAmount: float = field(init=False,default=0.00)
    total: float = field(init=False,default=0.00)    
    items: List[OrderItem] = field(default_factory=List[OrderItem])
    status: OrderStatusEnum = field(default=OrderStatusEnum.RECEIVED)
    # TODO implementar no futuro
    # address: Address = field(init=False, default_factory=Address)
    # payments: List[Payment] = field(init=False, default_factory=List[Payment])
    # payments: List[Payment] = field(init=False, default_factory=lambda : [])
    payments: List[Payment] = field(init=False, default=None)
    
    def calculate(self) -> float:
        self.total = self.deliveryAmount
        for item in self.items:    
            self.total = self.total + item.total
        return self.total                      
    