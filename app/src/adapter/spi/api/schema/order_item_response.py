from dataclasses import dataclass, field

@dataclass
class OrderItemResponse():
    productCode: str
    productName: str
    quantity: float
    amount: float = field(default=0.0)
    note: str = field(default=None)

    @property
    def total(self) -> float:
        return (self.amount * self.quantity)