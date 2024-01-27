from dataclasses import dataclass


@dataclass
class UserRequest:
    username: str
    password: str
    email: str