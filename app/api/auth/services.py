from jose import JWTError

from app.api.auth.auth_models_schemas import UserModel, UserRegister, UserRegisterResponse, TokenData, UserUpdate, Role
from app.api.auth.cryptographie import hash_password, verfiy_password
from app.api.auth.tokens import create_access_token, decode_access_token
from app.core.database import db_dependency
from app.core.config import ResourcePaths
from app.core.exceptions import BadRequestError, InvalidCredentialsError, NotFoundError


from fastapi import Depends, APIRouter, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


auth_router = APIRouter(prefix="/auth", tags=["auth"])
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")
templates = Jinja2Templates(directory=ResourcePaths.templates)


@auth_router.post(path="/register/",response_model=UserRegisterResponse, status_code=201)
async def create_user(user_register: UserRegister, db: db_dependency):
    existing_user = db.query(UserModel).filter(UserModel.username == user_register.username).first()
    if existing_user:
        raise BadRequestError

    hashed_password = hash_password(password=user_register.password)
    user = UserModel(username=user_register.username, password=hashed_password, email=user_register.email, is_active=user_register.is_active, role=user_register.role)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@auth_router.get(path="/users/")
async def get_all_users_from_db(db: db_dependency):
    return db.query(UserModel).all()


@auth_router.get("/current_user/", response_model=TokenData)
async def get_current_user(token: str = Depends(oauth_2_scheme)):
    try:
        
        payload = decode_access_token(token=token)    
        username: str = payload.get("sub")
        if username is None:
            raise InvalidCredentialsError
        token_data = TokenData(username=username)
        return token_data
        
    except JWTError:
        raise InvalidCredentialsError


@auth_router.get("/current_user/", response_model=TokenData)
async def login_for_access_token(db: db_dependency, form_data: OAuth2PasswordRequestForm = Depends()):

    user = db.query(UserModel).filter(UserModel.username == form_data.username).first()
    if not user:
        raise NotFoundError
    
    if verfiy_password(plain_password=form_data.password, password_hash=user.password):
        token = create_access_token(data={"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise InvalidCredentialsError    


@auth_router.put("/update_user/")
async def update_user(updated_user: UserUpdate, db: db_dependency, token_data: TokenData = Depends(get_current_user)):
    user = db.query(UserModel).filter(token_data.username == UserModel.username).first()
    if not user:
        raise NotFoundError
    
    if updated_user.username:
        user.username = updated_user.username
        
    if updated_user.email:
        user.email = updated_user.email
        
    if updated_user.password:
        user.password = hash_password(updated_user.password)
        
    if updated_user.is_active is not None:
        user.is_active = updated_user.is_active
        
    if updated_user.role:
        user.role = updated_user.role
        
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user


@auth_router.get("/login/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

