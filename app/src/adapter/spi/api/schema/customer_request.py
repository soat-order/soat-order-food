from dataclasses import dataclass, field


@dataclass
class CustomerRequest:
    name: str = field(default="")
    documentNumber: str = field(default="")
    email: str = field(default="")
    phoneNumber: str = field(default="")
