from pydantic import BaseModel, Field

from .mal_url import MalUrl

from utils import EnhancedEnum


class Anime(BaseModel):
    mal_id: int | None = Field(None, description='MyAnimeList ID')
    url: str | None = Field(None, description='MyAnimeList URL')
    images: AnimeImages | None = None
    trailer: TrailerBase | None = None
    approved: bool | None = Field(None, description='Whether the entry is pending approval on MAL or not')
    titles: list[Title] | None = Field(None, description='All titles')
    title: str | None = Field(None, deprecated=True, description='Title')
    title_english: str | None = Field(None, deprecated=True, description='English Title')
    title_japanese: str | None = Field(None, deprecated=True, description='Japanese Title')
    title_synonyms: list[str] | None = Field(None, deprecated=True, description='Other Titles')
    type: Type | None = Field(None, description='Anime Type')
    source: str | None = Field(None, description='Original Material/Source adapted from')
    episodes: int | None = Field(None, description='Episode count')
    status: Status | None = Field(None, description='Airing status')
    airing: bool | None = Field(None, description='Airing boolean')
    aired: Daterange | None = None
    duration: str | None = Field(None, description='Parsed raw duration')
    rating: Rating | None = Field(None, description='Anime audience rating')
    score: float | None = Field(None, description='Score')
    scored_by: int | None = Field(None, description='Number of users')
    rank: int | None = Field(None, description='Ranking')
    popularity: int | None = Field(None, description='Popularity')
    members: int | None = Field(None, description='Number of users who have added this entry to their list')
    favorites: int | None = Field(None, description='Number of users who have favorited this entry')
    synopsis: str | None = Field(None, description='Synopsis')
    background: str | None = Field(None, description='Background')
    season: Season | None = Field(None, description='Season')
    year: int | None = Field(None, description='Year')
    broadcast: Broadcast | None = None
    producers: list[MalUrl] | None = None
    licensors: list[MalUrl] | None = None
    studios: list[MalUrl] | None = None
    genres: list[MalUrl] | None = None
    explicit_genres: list[MalUrl] | None = None
    themes: list[MalUrl] | None = None
    demographics: list[MalUrl] | None = None


