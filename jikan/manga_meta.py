from pydantic import BaseModel, Field

from .manga_images import MangaImages


class MangaMeta(BaseModel):
    mal_id: int | None = Field(None, description='MyAnimeList ID')
    url: str | None = Field(None, description='MyAnimeList URL')
    images: MangaImages | None = None
    title: str | None = Field(None, description='Entry title')