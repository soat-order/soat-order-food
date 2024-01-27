from src.core.domain.user import User
from src.adapter.spi.api.schema.user_request import UserRequest
from src.adapter.spi.api.schema.user_create_request import UserCreateResquest


class UserMapper:
    @staticmethod
    def parseToDomain(request: UserRequest) -> User:
        domain = User(id=None,username=request.username, email=request.email)
        domain._password = request.password
        return domain

    @staticmethod
    def parseCreateToDomain(request: UserCreateResquest) -> User:
        domain = User(id=None,username=request.username, email=request.email)
        domain._password = request.password
        return domain
