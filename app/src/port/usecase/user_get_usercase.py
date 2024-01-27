from typing import List
from abc import ABC, abstractclassmethod
from src.core.domain.user import User


class UserGetUseCase(ABC):
    @abstractclassmethod
    def getByUsername(username: str) -> User:
        raise NotImplementedError
    
    @abstractclassmethod
    def getByUserValid(username: str, clientId: str) -> User:
        raise NotImplementedError    