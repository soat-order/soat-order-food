from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from src.port.usecase.user_post_usecase import UserPostUserCasePort
from src.core.usecase.user_post_usecase import UserPostUseCase
from src.core.domain.user_logged import UserLogged
from src.core.deps.deps import token_validade, login_validade
from src.core.auth.http_error import HttpForbidden
from src.adapter.spi.api.schema.user_create_request import UserCreateResquest
from src.adapter.spi.api.mapper.user_mapper import UserMapper



router = APIRouter()

security_schema = HTTPBasic()

__userPostUseCase: UserPostUserCasePort = UserPostUseCase()

@router.post(path="/login/token", status_code=status.HTTP_200_OK)
async def login(credentials: Annotated[HTTPBasicCredentials, Depends(security_schema)]):
    print(f"username: {credentials.username} | password: {credentials.password}")    
    return await login_validade(credentials.username, credentials.password)    

@router.post(path="/singup", status_code=status.HTTP_201_CREATED)
async def singup(user: UserCreateResquest):
    __userPostUseCase.create(UserMapper.parseCreateToDomain(user))

@router.get(path="/username/{username}", status_code=status.HTTP_200_OK)
async def getByUsername(username: str,userLogged : UserLogged = Depends(token_validade)):
    if (username != userLogged.username):
        raise HttpForbidden()
    return userLogged
