from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy import select, func
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from api.config.security_config import SecurityConfig
from api.db import get_db
from api.models import user as user_models
from api.schemas import user as user_schemas

async def create_user(db: AsyncSession, user_create: user_schemas.RequestCreateUser) -> user_models.User:

    result: Result = await db.execute(select(func.count(user_models.User.email)).filter(user_models.User.email == user_create.email))
    is_registed = result.all()[0][0]
    if is_registed != 0:
        return None

    user_create_dict = user_create.dict()
    hashed_password = SecurityConfig.pwd_ctx.hash(user_create.password)
    user_create_dict.pop("password")
    user_create_dict.update({"hashed_password": hashed_password})

    user = user_models.User(**user_create_dict)
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user

async def get_current_user(token: str = Depends(SecurityConfig.oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    
    try:
        payload = jwt.decode(token, SecurityConfig.SECRET_KEY, algorithms=[SecurityConfig.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    result: Result = await db.execute(select(user_models.User.email).filter(user_models.User.email == username))
    user = result.all()
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: user_models.User = Depends(get_current_user)):
    if len(current_user) != 1:
        raise HTTPException(status_code=400, deital="Inactive user")
    return current_user
