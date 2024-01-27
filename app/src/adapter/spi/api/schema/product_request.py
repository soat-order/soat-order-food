from dataclasses import dataclass, field, fields


@dataclass
class ProductRequest:
    code: str = field(default="")
    name: str = field(default="")
    amount: float = field(default=0.00)
    type: str = field(default="")

    # def __post_init__(self):
    #     # Loop through the fields
    #     for field in fields(self):
    #         # If there is a default and the value of the field is none we can assign a value
    #         if not isinstance(field.default, dataclasses._MISSING_TYPE) and getattr(self, field.name) is None:
    #             setattr(self, field.name, field.default)
