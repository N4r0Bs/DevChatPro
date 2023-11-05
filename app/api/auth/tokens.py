from jose import JWTError, jwt
from datetime import datetime, timedelta

from fastapi.security import  OAuth2PasswordBearer
from fastapi import Depends

from app.core.config import jwt_config
from app.core.exceptions import InvalidCredentialsError
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="auth/Token")


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta is None:
        expires_delta = timedelta(minutes=jwt_config.access_token_expire_minutes)        
    else:
        expires_delta = timedelta(minutes=15)
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=jwt_config.access_token_expire_minutes))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(claims=to_encode, key=jwt_config.secret_key, algorithm=jwt_config.algorithm)
    return encoded_jwt  


def decode_access_token(token: str = Depends(oauth_2_scheme)):
    try:
        payload = jwt.decode(token=token, key=jwt_config.secret_key, algorithms=jwt_config.algorithm)
        return payload
    
    except JWTError:
        raise InvalidCredentialsError


    

    