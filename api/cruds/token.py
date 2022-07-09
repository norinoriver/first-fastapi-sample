from typing import Union
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select
from jose import jwt
from api.config.security_config import SecurityConfig
from api.models import user as user_model

# TODO: move to core
def verify_password(plain_password, hashed_password):
    return SecurityConfig.pwd_ctx.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SecurityConfig.SECRET_KEY, algorithm=SecurityConfig.ALGORITHM)
    return encoded_jwt

async def authenticate_user(form_data: OAuth2PasswordRequestForm, db: AsyncSession):
    result: Result = await db.execute(select(user_model.User.email, user_model.User.hashed_password).filter(user_model.User.email == form_data.username))
    user = result.all()[0]
    if not user:
        return False

    if not verify_password(form_data.password, user.hashed_password):
        return False

    return user
