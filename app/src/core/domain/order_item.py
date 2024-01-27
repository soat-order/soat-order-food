from dataclasses import dataclass, field

@dataclass
class OrderItem():
    productId: str = field(init=False, default=None)
    productCode: str
    productName: str = field(init=False)
    quantity: float
    amount: float = field(default=0.0)
    note: str = field(default=None)

    @property
    def total(self) -> float:
        return (self.amount * self.quantity)