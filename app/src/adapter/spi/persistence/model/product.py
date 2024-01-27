import uuid
from dataclasses import dataclass, field


# https://www.mongodb.com/community/forums/t/why-do-we-need-alias-id-in-pydantic-model-of-fastapi/170728

@dataclass
class Product():
    _id: str = field(init=False)
    code: str
    name: str
    amount: float
    type: str

    def __post_init__(self):
        self._id = str(uuid.uuid4())

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value
