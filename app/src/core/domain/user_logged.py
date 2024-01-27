from dataclasses import dataclass

@dataclass
class UserLogged():
    id: str
    username: str
    clientId: str