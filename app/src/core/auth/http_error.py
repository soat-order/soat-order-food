from typing import Any, Dict, Optional
from fastapi import HTTPException, status


class HttpUnauthorized(HTTPException):
    def __init__(self, message: Optional[str] = f"{status.HTTP_401_UNAUTHORIZED} Unauthorized") -> None:
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED,
                                            detail=message,
                                            headers={"WWW-Authenticate": "Bearer"})
        
class HttpForbidden(HTTPException):
    def __init__(self, message: Optional[str] = f"{status.HTTP_403_FORBIDDEN} Forbidden") -> None:
        super().__init__(status_code=status.HTTP_403_FORBIDDEN,
                                            detail=message,
                                            headers={"WWW-Authenticate": "Bearer"})        