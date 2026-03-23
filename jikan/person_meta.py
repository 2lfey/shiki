from pydantic import BaseModel, Field

from .people_images import PeopleImages


class PersonMeta(BaseModel):
    mal_id: int | None = Field(None, description='MyAnimeList ID')
    url: str | None = Field(None, description='MyAnimeList URL')
    images: PeopleImages | None = None
    name: str | None = Field(None, description='Entry name')