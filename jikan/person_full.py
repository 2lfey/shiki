from pydantic import BaseModel, Field

from .people_images import PeopleImages


class AnimeItem(BaseModel):
    position: str | None = Field(None, description="Person's position")
    anime: AnimeMeta | None = None


class MangaItem(BaseModel):
    position: str | None = Field(None, description="Person's position")
    manga: MangaMeta | None = None


class Voice(BaseModel):
    role: str | None = Field(None, description="Person's Character's role in the anime")
    anime: AnimeMeta | None = None
    character: CharacterMeta | None = None


class PersonFull(BaseModel):
    mal_id: int | None = Field(None, description='MyAnimeList ID')
    url: str | None = Field(None, description='MyAnimeList URL')
    website_url: str | None = Field(None, description="Person's website URL")
    images: PeopleImages | None = None
    name: str | None = Field(None, description='Name')
    given_name: str | None = Field(None, description='Given Name')
    family_name: str | None = Field(None, description='Family Name')
    alternate_names: list[str] | None = Field(None, description='Other Names')
    birthday: str | None = Field(None, description='Birthday Date ISO8601')
    favorites: int | None = Field(None, description='Number of users who have favorited this entry')
    about: str | None = Field(None, description='Biography')
    anime: list[AnimeItem] | None = None
    manga: list[MangaItem] | None = None
    voices: list[Voice] | None = None