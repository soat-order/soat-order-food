from dataclasses import dataclass, field


@dataclass
class CustomerInactiveRequest:
    inactive: bool
