from fastapi import status,  HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db
import api.cruds.user as user_cruds
import api.schemas.user as user_schemas

router = APIRouter()

@router.post("/", response_model=user_schemas.ResponseUser)
async def register_new_user(user_body: user_schemas.RequestCreateUser, db: AsyncSession = Depends(get_db)):
    user = await user_cruds.create_user(db, user_body)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't use this email.",
        )

    return user

@router.get("/users/me/")
async def read_users_me(current_user: user_schemas.ResponseUser = Depends(user_cruds.get_current_active_user)):
    return current_user