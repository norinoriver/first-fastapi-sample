from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.orm import relationship
from api.db import Base

class User(Base):
    __tablename__ = "users"

    userid = Column(Integer, primary_key=True)
    hashed_password = Column(String(60), nullable=False)
    email = Column(String(256), unique=True, nullable=False)
    permit_url = Column(String(32), unique=True, nullable=False)
    permit_deadline = Column(DateTime, nullable=False)
    is_permitted = Column(Boolean, default=False, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)