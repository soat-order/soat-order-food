import uuid
from dataclasses import dataclass, field
from datetime import datetime
from src.core.util.string_util import StringUtil


@dataclass
class User:
    _id: str = field(init=False)
    username: str
    password: str
    email: str
    inactive: bool = field(init=False,default=False)
    datatimeCreate: datetime = field(init=False,default=datetime.now())

    def __post_init__(self):
        self._id = str(uuid.uuid4())
        self.password = StringUtil.parseUUID(self.password)
        # self.inactive = False
        # self.datatimeCreate = datetime.now()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

