from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from api.config.config import DBConfig

ASYNC_DB_URL = "mysql+aiomysql://" + DBConfig().__str__()

async_engine=create_async_engine(ASYNC_DB_URL, echo=True)
async_session= sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

Base = declarative_base()

async def get_db():
    async with async_session() as session:
        yield session