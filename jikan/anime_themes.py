from pydantic import BaseModel

from .theme import Theme


class AnimeThemes(BaseModel):
    data: Theme | None = None