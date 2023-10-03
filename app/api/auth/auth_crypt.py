from typing import Optional
from jose import jwt

import hashlib

import base64
import bcrypt


def hash_to_sha256(input_bytestring: bytes) -> bytes:
    if not isinstance(input_bytestring, bytes):
        input_bytestring = str(input_bytestring).encode("UTF-8")
            
    return base64.b64encode(hashlib.sha256(input_bytestring).digest())


def hash_password(password:str, salt: Optional[bytes] = None) -> str:
    if salt is None:
        salt = bcrypt.gensalt(rounds=12)
    password = password.encode("UTF-8")
    
    return bcrypt.hashpw(password=hash_to_sha256(input_bytestring=password), salt=salt).decode()


def verfiy_password(plain_password: str, password_hash: str) -> bool:
    plain_password = hash_to_sha256(plain_password)
    password_hash = password_hash.encode("UTF-8")
    
    return bcrypt.checkpw(password=plain_password, hashed_password=password_hash)