from dataclasses import dataclass, field
from typing import List
from src.adapter.spi.api.schema.order_item_request import OrderItemRequest


@dataclass
class OrderRequest:
    id: str = field(init=False, default=None)
    customerName: str = field(default=None)
    customerIdentify: str = field(default=None)
    # TODO implementar a parte de entrega em outra fase
    # address: AddressRequest = field(init=False, default_factory=Address)
    items: List[OrderItemRequest] = field(default_factory=List[OrderItemRequest])
