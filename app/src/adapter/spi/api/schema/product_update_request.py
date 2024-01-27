from dataclasses import dataclass, field


@dataclass
class ProductUpdateRequest:
    id: str = field(default=None)
    name: str = field(default=None)
    amount: float = field(default=None)
    type: str = field(default=None)

