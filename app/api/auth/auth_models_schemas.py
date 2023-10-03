from app.core.database import Model
from pydantic import BaseModel


from sqlalchemy import Integer, String, Boolean, Column, DATETIME, Enum
from enum import Enum as Enumaration
from datetime import datetime

class Role(Enumaration):
    ADMIN = "Admin"
    MEMBER = "Member"


class UserModel(Model):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    email = Column(String(100), index=True, nullable=False, unique=True)
    is_active = Column(Boolean, default=True, index=True, nullable=False)
    registered_at = Column(DATETIME, default=datetime.utcnow, nullable=False)
    role = Column(Enum(Role), default=Role.MEMBER, index=True)
    
class UserRegister(BaseModel):
    username: str
    password: str
    email: str
    is_active: bool
    role: Role
    
class UserRegisterResponse(BaseModel):
    username: str
    email: str
    is_active: bool
    role: Role