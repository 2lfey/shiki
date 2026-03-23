from pydantic import BaseModel, Field


class MangaItem(BaseModel):
    position: str | None = Field(None, description="Person's position")
    manga: MangaMeta | None = None


class PersonManga(BaseModel):
    data: list[MangaItem] | None = None