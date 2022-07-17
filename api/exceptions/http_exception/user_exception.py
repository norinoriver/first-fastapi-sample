from enum import Enum
from fastapi import HTTPException, status

class UserException(Enum):
    COULD_NOT_VALIDATE_CREDENTIALS = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    INCORRECT_USERNAME_OR_PASSWORD = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password", 
        headers={"WWW-Authenticate": "Bearer"}
    )

    INACTIVE_USER = HTTPException(
        status_code=400, 
        detail="Inactive user"
    )

    CANNOT_USE_EMAIL = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Can't use this email."
    )