from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class RequestCreateUser(UserBase):
    password: str

class ResponseUser(UserBase):
    
    class Config:
        orm_mode = True

