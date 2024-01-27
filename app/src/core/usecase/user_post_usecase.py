from src.port.spi.persistence.repository.repository import Repository
from src.port.usecase.user_post_usecase import UserPostUserCasePort
from src.adapter.spi.persistence.repository.user_repository import UserRepository
from src.adapter.spi.persistence.mapper.user_mapper import UserMapper
from src.core.domain.user import User
from src.core.util.logger_custom import Logger


class UserPostUseCase(UserPostUserCasePort):
    def __init__(self) -> None:
        super().__init__()
        self.__repository : Repository = UserRepository()

    def create(self, user: User) -> User:
        Logger.info(method=Logger.getMethodCurrent(), message="Start of use case to save user")
        return UserMapper.parseToDomain(self.__repository.save(UserMapper.parseToModel(user)))