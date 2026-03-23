from pydantic import BaseModel, Field

from .anime_meta import AnimeMeta


class AnimeItem(BaseModel):
    entry: AnimeMeta | None = None
    score: int | None = None
    status: str | None = None
    episodes_seen: int | None = None
    episodes_total: int | None = None
    date: str | None = Field(None, description='ISO8601 format')