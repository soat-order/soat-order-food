from datetime import datetime, timezone, timedelta
from jwt import PyJWT
from fastapi.security import HTTPBearer
from src.config.settings_config import settings
from src.port.spi.persistence.repository.repository import Repository
from src.core.domain.user import User
from src.core.domain.user_logged import UserLogged
from src.core.auth.http_error import HttpUnauthorized
from src.core.auth.schema.token_response import TokenResponse as Token
from src.core.auth.schema.token_decode import TokenDecode
from src.core.auth.mapper.token_mapper import TokenMapper
from src.adapter.spi.persistence.mapper.user_mapper import UserMapper
from src.adapter.spi.persistence.repository.user_repository import UserRepository


bearer_schema = HTTPBearer()

class AuthToken():
    def __init__(self) -> None:
        self.__repository = UserRepository()
        self.__jwt  = PyJWT()
        self.__credential_exception = HttpUnauthorized()

    # https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3
    # https://jwt.io
    async def __create_token(self, username: str, clientId: str) -> Token:
        tz_sp = timezone(offset=timedelta(hours=-3), name='America/Sao_Paulo')
        iat = datetime.now(tz=tz_sp)
        datetime_expire = iat + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTE)
        payload = {
            'type': settings.ALGORITHM,
            'exp': datetime_expire,
            'iat': iat,
            'sub': f"{username}|{clientId}"
        }
        token: str = self.__jwt.encode(payload=payload, key=settings.JWT_SECRET_ID, 
                                       algorithm=settings.ALGORITHM)        
        return Token(access_token=token, type_token=settings.ALGORITHM, expire_token=datetime_expire)
        
    async def __decode_token(self, token: str) -> UserLogged:
        try:
            payload = self.__jwt.decode(jwt=token, key=settings.JWT_SECRET_ID,
                                        algorithms=settings.ALGORITHM, do_verify=False)
            tokenDecode : TokenDecode = TokenMapper.parseToTokenDecode(token=payload)
            if (tokenDecode is None or tokenDecode.expired()
                or tokenDecode.getClientId() is None):
                raise self.__credential_exception
            user: User = UserMapper.parseToDomain(self.__repository.getByUsername(username=tokenDecode.getUsername()))
            if (user is None or not user.validatePasswd(tokenDecode.getClientId())):
                raise self.__credential_exception
            return UserLogged(id=user.id, username=user.username, clientId=user.clientId)
        except Exception as ex:
            raise self.__credential_exception
        
    async def validate_login(self, username: str, password: str):
        user : User = UserMapper.parseToDomain(self.__repository.getByUsername(username=username))
        if ((user is not None)
            and (user.validatePasswd(password))):
            return await self.__create_token(username=user.username, clientId=user.clientId)
        raise self.__credential_exception
        
    async def validate_token(self, token: str) -> UserLogged:
        return await self.__decode_token(token)
