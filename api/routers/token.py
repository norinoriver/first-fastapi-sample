from datetime import timedelta
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from api.exceptions.http_exception.user_exception import UserException
from api.config.security_config import SecurityConfig
from api.schemas import token as token_schemas
from api.cruds import token as token_cruds
from api.db import get_db

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/token", response_model=token_schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    # TODO: access to rdb and redis logic
    user = await token_cruds.authenticate_user(form_data, db)
    if not user:
        raise UserException.INCORRECT_USERNAME_OR_PASSWORD
    access_token_expires = timedelta(minutes=SecurityConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token_cruds.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}