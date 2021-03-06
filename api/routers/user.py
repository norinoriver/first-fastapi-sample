from fastapi import status,  HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db
import api.cruds.user as user_cruds
import api.schemas.user as user_schemas
from api.exceptions.http_exception.user_exception import UserException

router = APIRouter()

@router.post("/", response_model=user_schemas.ResponseCreatedUser)
async def create_new_user(user_body: user_schemas.RequestCreateUser, db: AsyncSession = Depends(get_db)):
    if await user_cruds.is_registed_user(db, user_body):
        raise UserException.CANNOT_USE_EMAIL
        
    user = await user_cruds.create_user(db, user_body)
    
    return user

@router.put("/users/permit/{uuid}", response_model=user_schemas.ResponseUser)
async def user_permit(uuid: str, db: AsyncSession = Depends(get_db)):
    not_permit_user = await user_cruds.is_permitted_user(uuid, db)
    if not not_permit_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
        )

    return await user_cruds.update_permmit_user(not_permit_user, db)

@router.get("/users/me/")
async def read_users_me(current_user: user_schemas.ResponseUser = Depends(user_cruds.get_current_active_user)):
    return current_user