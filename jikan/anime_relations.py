from pydantic import BaseModel, Field

from .relation import Relation


class AnimeRelations(BaseModel):
    data: list[Relation] | None = None