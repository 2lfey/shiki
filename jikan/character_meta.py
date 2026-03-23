from pydantic import BaseModel, Field

from .character_images import CharacterImages


class CharacterMeta(BaseModel):
    mal_id: int | None = Field(None, description='MyAnimeList ID')
    url: str | None = Field(None, description='MyAnimeList URL')
    images: CharacterImages | None = None
    name: str | None = Field(None, description='Entry name')