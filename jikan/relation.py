from pydantic import BaseModel, Field

from .mal_url import MalUrl


class Relation(BaseModel):
    relation: str | None = Field(None, description='Relation type')
    entry: list[MalUrl] | None = Field(None, description='Related entries')