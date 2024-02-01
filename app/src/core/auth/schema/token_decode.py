from dataclasses import dataclass, field

@dataclass
class TokenDecode:
    type: str
    exp: int
    iat: int
    sub: str
    _username: str = field(init=False)
    _clientId: str = field(init=False)

    def __post_init__(self):
        self._username, separator, self._clientId = str(self.sub).partition("|")

    def expired(self) -> bool:
        return (self.exp < self.iat)
    
    def getUsername(self) -> str:
        return self._username
        
    def getClientId(self) -> str:
        return self._clientId