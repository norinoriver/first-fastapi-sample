import os
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

class SecurityConfig:
    pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    SECRET_KEY = os.environ.get("API_SECRET_KEY")
    ALGORITHM = os.environ.get("API_SECRET_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = 30