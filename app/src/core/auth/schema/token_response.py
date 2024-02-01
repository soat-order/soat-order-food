from dataclasses import dataclass


@dataclass
class TokenResponse:
    access_token: str
    expire_token: int
    type_token: str