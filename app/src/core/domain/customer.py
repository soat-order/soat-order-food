from dataclasses import dataclass, field


@dataclass
class Customer():
    id: str = field(init=False, default=None)
    name: str
    documentNumber: str
    email: str
    phoneNumber: str
