"""Database models for the application, using SQLModel for data validation and SQLAlchemy for ORM."""

from typing import List, Optional

from sqlmodel import SQLModel, Field, Relationship


class SongBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None


class Song(SongBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class SongCreate(SongBase):
    pass


class GenreBase(SQLModel):
    name: str


class Genre(GenreBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    artists: List["Artist"] = Relationship(back_populates="genre")


class GenreCreate(GenreBase):
    pass


class Artist(SQLModel, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    name: str
    # a relation to Genre
    genre: Genre = Relationship(back_populates="artists")


class ShowBase(SQLModel):
    venue: str
    date: str
    time: str


class Show(ShowBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    # a relation to Artist
    artists: List[Artist] = Relationship(back_populates="shows")


class ShowCreate(ShowBase):
    pass
