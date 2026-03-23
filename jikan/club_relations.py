from pydantic import BaseModel

from utils import DataModel

from .mal_url import MalUrl


class ClubRelation(BaseModel):
    anime: list[MalUrl] | None = None
    manga: list[MalUrl] | None = None
    characters: list[MalUrl] | None = None


class ClubRelations(DataModel[ClubRelation])