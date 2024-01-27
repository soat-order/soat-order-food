from dataclasses import dataclass, field


@dataclass
class OrderItemRequest:
    productCode: str = field(default=None)
    quantity: float = field(default=None)
    note: str = field(default=None)
