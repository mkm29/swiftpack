"""Database models for the application, using SQLModel for data validation and SQLAlchemy for ORM."""

from sqlmodel import SQLModel, Field
from typing import Optional


class SongBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None


class Song(SongBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class SongCreate(SongBase):
    pass