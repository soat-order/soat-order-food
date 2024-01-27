from dataclasses import dataclass, field
from src.core.util.string_util import StringUtil


@dataclass
class User:
    id: str = field(default=None)
    username: str = field(default=None)
    _password: str = field(init=False, default=None)
    email: str = field(default=None)

    def validatePasswd(self, passwd: str) -> bool:
        passwd = passwd if (StringUtil.validateUUID(passwd)) else StringUtil.parseUUID(passwd)
        return self._password == passwd

    @property
    def clientId(self) -> str:
        return self._password