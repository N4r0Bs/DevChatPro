from sqlalchemy.orm import Session

from app.api.auth.auth_models_schemas import UserModel, UserRegister, UserRegisterResponse
from app.api.auth.auth_crypt import hash_password
from app.core.database import db_session

from fastapi import HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestFormStrict
auth_router = APIRouter()


@auth_router.post(path="/register/",response_model=UserRegisterResponse, status_code=201)
async def create_user(user_register: UserRegister, db: Session = Depends(db_session)):
     
    existing_user = db.query(UserModel).filter(UserModel.username == user_register.username).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already in use")
    
    hashed_password = hash_password(password=user_register.password)
    user = UserModel(username=user_register.username, password=hashed_password, email=user_register.email, is_active=user_register.is_active, role=user_register.role )

    db.add(user)
    db.commit()
    db.refresh(user)
    return {""}


@auth_router.get(path="/users/")
async def get_all_users_from_db(db: Session = Depends(db_session)):
    return db.query(UserModel).all()
