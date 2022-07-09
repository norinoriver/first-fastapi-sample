from enum import unique
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.db import Base

class User(Base):
    __tablename__ = "users"

    userid = Column(Integer, primary_key=True)
    hashed_password = Column(String(60))
    email = Column(String(256), unique=True)