from typing import Optional, Union
from starlette.exceptions import HTTPException
from starlette import status

# Token-bezogene Ausnahmen
class TokenException(HTTPException):
    def __init__(self, status_code: int, detail: Union[str, None] = None, headers: Union[dict, None] = None) -> None:
        super().__init__(status_code, detail, headers)

class InvalidTokenError(TokenException):
    def __init__(self, detail: Union[str, None] = "Invalid Token", headers: Union[dict, None] = {"WWW-Authenticate": "Bearer"}) -> None:
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail, headers)

class ExpiredTokenError(TokenException):
    def __init__(self, detail: Union[str, None] = "Expired Token", headers: Union[dict, None] = {"WWW-Authenticate": "Bearer"}) -> None:
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail, headers)

class InvalidCredentialsError(TokenException):
    def __init__(self, detail: Union[str, None] = "Invaild Credentials", headers: Union[dict, None] = {"WWW-Authenticate": "Bearer"}) -> None:
        super().__init__(status.HTTP_401_UNAUTHORIZED, detail, headers)

# API-Datenbankabfrage-Ausnahmen
class DatabaseQueryException(HTTPException):
    def __init__(self, status_code: int, detail: Union[str, None] = None, headers: Union[dict, None] = None) -> None:
        super().__init__(status_code, detail, headers)

class NotFoundError(DatabaseQueryException):
    def __init(self, detail: Union[str, None] = "Resource Not Found", headers: Union[dict, None] = None) -> None:
        super().__init(status.HTTP_404_NOT_FOUND, detail, headers)

class BadRequestError(DatabaseQueryException):
    def __init(self, detail: Union[str, None] = "Bad Request", headers: Union[dict, None] = None) -> None:
        super().__init(status.HTTP_400_BAD_REQUEST, detail, headers)

class UsernameNotAcceptable(DatabaseQueryException):
    def __init(self, detail: Union[str, None] = "Username not Accepted ", headers: Union[dict, None] = None) -> None:
        super().__init(status.HTTP_406_NOT_ACCEPTABLE, detail, headers)

