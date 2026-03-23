from pydantic import BaseModel, Field

from .character import Character
from .anime_item import AnimeItem
from .manga_item import MangaItem
from .voice import Voice


class CharacterFull(Character):
    anime: list[AnimeItem] | None = None
    manga: list[MangaItem] | None = None
    voices: list[Voice] | None = None