from pydantic import BaseModel, Field


class MalUrl(BaseModel):
    mal_id: int | None = Field(None, description='MyAnimeList ID')
    type: str | None = Field(None, description='Type of resource')
    name: str | None = Field(None, description='Resource Name/Title')
    url: str | None = Field(None, description='MyAnimeList URL')


class MalUrl2(BaseModel):
    mal_id: int | None = Field(None, description='MyAnimeList ID')
    type: str | None = Field(None, description='Type of resource')
    title: str | None = Field(None, description='Resource Name/Title')
    url: str | None = Field(None, description='MyAnimeList URL')