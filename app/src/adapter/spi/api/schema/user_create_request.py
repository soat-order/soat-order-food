from dataclasses import dataclass


@dataclass
class UserCreateResquest:
    username: str
    password: str
    email: str