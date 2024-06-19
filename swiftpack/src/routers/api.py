"""API router for the songs API routes"""

from fastapi import Depends
from fastapi import APIRouter
from sqlmodel import Session, select

from swiftpack.src.db.models import Song, SongCreate
from swiftpack.src.db import get_session

router = APIRouter()


@router.get("/songs", response_model=list[Song])
async def get_songs(*, session: Session = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]


@router.post("/songs")
async def add_song(*, session: Session = Depends(get_session), song: SongCreate):
    song = Song(name=song.name, artist=song.artist, year=song.year)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song
