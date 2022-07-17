from datetime import datetime, timedelta
import uuid
import urllib
from fastapi import Depends
from jose import JWTError, jwt
from sqlalchemy import select, func
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from api.config.security_config import SecurityConfig
from api.config.server_config import ServerConfig
from api.db import get_db
from api.models import user as user_models
from api.schemas import user as user_schemas
from api.exceptions.http_exception.user_exception import UserException

async def is_registed_user(db: AsyncSession, target_user: user_schemas.RequestCreateUser):
    result: Result = await db.execute(select(func.count(user_models.User.email)).filter(user_models.User.email == target_user.email))
    result_list = result.all()
    is_registed = result_list[0][0]
    if is_registed == 0:
        return False
    else:
        return True

async def create_user(db: AsyncSession, user_create: user_schemas.RequestCreateUser) -> user_models.User:
    user_create_dict = user_create.dict()
    hashed_password = SecurityConfig.pwd_ctx.hash(user_create.password)
    user_create_dict.pop("password")
    user_create_dict.update({"hashed_password": hashed_password})
    user_create_dict.update({"permit_url": uuid.uuid4().hex})
    datetime_now = datetime.now()
    permit_deadline = datetime_now + timedelta(days=1)
    user_create_dict.update({"permit_deadline": permit_deadline.__str__()})

    user = user_models.User(**user_create_dict)
    db.add(user)

    await db.commit()
    await db.refresh(user)

    user.permit_url = ServerConfig().__str__() + urllib.parse.quote(user.permit_url)
    return user

async def is_permitted_user(uuid, db: AsyncSession):
    result: Result = await db.execute(
        select(user_models.User)
            .filter(user_models.User.permit_url == uuid)
            .filter(user_models.User.permit_deadline >= datetime.now())
            .filter(user_models.User.is_permitted == False)
    )

    not_permitted_user = result.first()

    if not not_permitted_user:
        return None

    not_permitted_user: user_models.User = not_permitted_user[0]
    return not_permitted_user

async def update_permmit_user(user: user_schemas.ResponsePermitedUser, db: AsyncSession):
    user.is_permitted = True
    await db.commit()
    await db.refresh(user)
    return user


async def get_current_user(token: str = Depends(SecurityConfig.oauth2_scheme), db: AsyncSession = Depends(get_db)):
    try:
        payload = jwt.decode(token, SecurityConfig.SECRET_KEY, algorithms=[SecurityConfig.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise UserException.COULD_NOT_VALIDATE_CREDENTIALS
    except JWTError:
        raise UserException.COULD_NOT_VALIDATE_CREDENTIALS
    
    result: Result = await db.execute(select(user_models.User.userid, user_models.User.email).filter(user_models.User.email == username))
    user = result.all()
    if user is None:
        raise UserException.COULD_NOT_VALIDATE_CREDENTIALS
    return user

async def get_current_active_user(current_user: user_models.User = Depends(get_current_user)):
    if len(current_user) != 1:
        raise UserException.INACTIVE_USER
    return current_user[0]