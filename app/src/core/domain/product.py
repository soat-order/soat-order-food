from dataclasses import dataclass, field
from src.core.domain.enum.producty_type_enum import ProductType


@dataclass
class Product:
    id: str = field(init=False, default=None)
    code: str
    name: str
    amount: float
    type: ProductType
