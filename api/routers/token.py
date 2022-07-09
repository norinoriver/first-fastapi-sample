from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
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
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password", # TODO: move to enum or config file
            headers={"WWW-Authenticate": "Bearer"} # TODO: move to enum or config file
        )
    access_token_expires = timedelta(minutes=SecurityConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token_cruds.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}