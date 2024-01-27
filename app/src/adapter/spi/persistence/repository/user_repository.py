from src.adapter.spi.persistence.model.user import User
from src.adapter.spi.persistence.repository.repository_default import RepositoryDefault
from src.adapter.spi.persistence.mapper.user_mapper import UserMapper


class UserRepository(RepositoryDefault):
    def __init__(self) -> None:
        super().__init__(User)

    def getByUsername(self, username: str) -> User:
        return self.parseToModel(self._getSession().find_one({'username': username, 'inactive': False}))        

    def parseToModel(self, dict: dict) -> User:
        return UserMapper.parseDictToModel(dict)
