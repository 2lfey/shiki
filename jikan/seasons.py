from pydantic import BaseModel, Field


class YearSeasons(BaseModel):
    year: int | None = Field(None, description='Year')
    seasons: list[str] | None = Field(None, description='List of available seasons')


class Seasons(BaseModel):
    data: list[YearSeasons] | None = None