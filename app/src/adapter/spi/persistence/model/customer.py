from dataclasses import dataclass, field
import uuid

@dataclass
class Customer():
    _id: str = field(init=False)
    name: str
    documentNumber: str
    email: str
    phoneNumber: str
    inactive: bool = field(init=False, default=False)

    def __post_init__(self):
        self.id = str(uuid.uuid4())

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value