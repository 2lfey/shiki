from pydantic import BaseModel

from enum import Enum


class GenreEntryType(Enum):
    ANIME = "Anime"
    MANGA = "Manga"


class Genre(BaseModel):
    id: int
    kind: GenreKind
    name: str
    russian: str
    entry_type: GenreEntryType