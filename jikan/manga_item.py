from pydantic import BaseModel, Field

from .manga_meta import MangaMeta


class MangaItem(BaseModel):
    entry: MangaMeta | None = None
    score: int | None = None
    status: str | None = None
    chapters_read: int | None = None
    chapters_total: int | None = None
    volumes_read: int | None = None
    volumes_total: int | None = None
    date: str | None = Field(None, description='ISO8601 format')