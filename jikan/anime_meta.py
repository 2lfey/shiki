from pydantic import BaseModel, Field

from .anime_images import AnimeImages


class AnimeMeta(BaseModel):
    mal_id: int | None = Field(None, description='MyAnimeList ID')
    url: str | None = Field(None, description='MyAnimeList URL')
    images: AnimeImages | None = None
    title: str | None = Field(None, description='Entry title')