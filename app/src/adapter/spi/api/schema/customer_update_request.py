from dataclasses import dataclass, field


@dataclass
class CustomerUpdateRequest:
    id: str = field(default="")
    name: str = field(default="")
    email: str = field(default="")
    phoneNumber: str = field(default="")
