from abc import ABC, abstractmethod
from src.core.domain.user import User

class UserPostUserCasePort(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        raise NotImplementedError