from dataclasses import dataclass, field


@dataclass
class CustomerResponse():
    id: str
    name: str
    documentNumber: str = field(metadata={"name": 'document_number'})
    email: str
    phoneNumber: str
