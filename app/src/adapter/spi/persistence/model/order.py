import uuid
from typing import List
from datetime import datetime
from dataclasses import dataclass, field
from decimal import *
from src.adapter.spi.persistence.model.order_item import OrderItem

@dataclass
class Order:
    _id: str = field(init=False, default=None)
    issueDateTime: datetime = field(init=False, default=datetime.now())
    customerName: str = field(default=None)
    customerIdentify: str = field(default=None)
    # zipCode: str = field(default=None)
    # country: int = field(default="BR")
    # state: str = field(default=None)
    # city: str = field(default=None) 
    # address: str = field(default=None)
    deliveryAmount: float = field(default=0.00)
    totalAmount: float = field(default=0.00)
    status: str = field(default=None)
    items: List[OrderItem] = field(default_factory=List[OrderItem])    
    
    def __post_init__(self):
        self.id = str(uuid.uuid4())

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value
