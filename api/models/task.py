from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))

    done = relationship("Done", back_populates="task")

class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey("task.id"), primary_key=True)

    task = relationship("Task", back_populates="done")