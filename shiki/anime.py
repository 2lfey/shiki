from pydantic import BaseModel

from enum import Enum
from typing import Optional

from . import Image


class Kind(Enum):
    TV = "tv"
    TV_13 = "tv_13" # Может не быть вообще, нужно проверить
    TV_24 = "tv_24" # Может не быть вообще, нужно проверить
    TV_48 = "tv_48" # Может не быть вообще, нужно проверить
    MOVIE = "movie"
    OVA = "ova"
    ONA = "ona"
    SPECIAL = "special"
    TV_SPECIAL = "tv_special"
    MUSIC = "music"
    PV = "pv"
    CM = "cm"


class Status(Enum):
    ANONS = "anons"
    ONGOING = "ongoing"
    RELEASED = "released"


class AnimeListItem(BaseModel):
    id: int
    name: str
    russian: str
    image: Image # Нужно смотреть какие поля есть
    url: str
    kind: Kind
    score: float
    status: Status
    episodes: int
    episodes_aired: int
    aired_on: Optional[str] # "2014-01-01",
    released_on: Optional[str]