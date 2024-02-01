from typing import Annotated
from src.core.domain.user_logged import UserLogged
from src.core.auth.auth_token import AuthToken
from src.core.auth.schema.token_response import TokenResponse
from src.core.util.logger_custom import Logger
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials



bearer_schema = HTTPBearer()

__authToken: AuthToken  = AuthToken()

async def token_validade(tokenBearer: Annotated[HTTPAuthorizationCredentials, Depends(bearer_schema)]) -> UserLogged:
    Logger.info("Deps.token_validade", f"Start validate token by scheme {tokenBearer.scheme} and credentials: {tokenBearer.credentials}")
    return await __authToken.validate_token(token=tokenBearer.credentials)

async def login_validade(username: str, password: str) -> TokenResponse:
    Logger.info("Deps.login_validade", f"Start validate login by scheme basicAuth and username {username}")
    return await __authToken.validate_login(username=username, password=password)
