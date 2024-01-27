from dataclasses import dataclass


@dataclass
class ProductResponse:
    id: str
    code: str
    name: str
    amount: float
    type: str
