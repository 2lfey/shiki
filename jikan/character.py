from pydantic import BaseModel, Field

from .character_item import CharacterItem


class Character(CharacterItem):
    name_kanji: str | None = Field(None, description='Name')
    nicknames: list[str] | None = Field(None, description='Other Names')
    favorites: int | None = Field(None, description='Number of users who have favorited this entry')
    about: str | None = Field(None, description='Biography')