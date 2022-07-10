from datetime import datetime
from pydantic import BaseModel, EmailStr, HttpUrl, AnyHttpUrl

class UserBase(BaseModel):
    email: EmailStr

class RequestCreateUser(UserBase):
    password: str

class ResponseUser(UserBase):
    
    class Config:
        orm_mode = True

class ResponseCreatedUser(UserBase):
    permit_url: AnyHttpUrl
    permit_deadline: datetime

    class Config:
        orm_mode = True

class ResponsePermitedUser(UserBase):
    userid: int
    is_permitted: bool

    class Config:
        orm_mode = True