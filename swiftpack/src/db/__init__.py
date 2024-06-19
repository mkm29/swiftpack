"""Database module to create engine and session for database operations."""

from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from swiftpack.src.config import Settings


# function to create engine
def get_engine():
    database_url: str = Settings().database_url
    engine = create_async_engine(database_url, echo=True, future=True)
    return engine


async def init_db():
    async with get_engine().begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(get_engine(), class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
