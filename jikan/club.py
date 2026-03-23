from pydantic import BaseModel, Field

from .common_images import CommonImages


class Club(BaseModel):
    mal_id: int | None = Field(None, description='MyAnimeList ID')
    name: str | None = Field(None, description='Club name')
    url: str | None = Field(None, description='Club URL')
    images: CommonImages | None = None
    members: int | None = Field(None, description='Number of club members')
    category: Category | None = Field(None, description='Club Category')
    created: str | None = Field(None, description='Date Created ISO8601')
    access: Access | None = Field(None, description='Club access')