from pydantic import BaseModel, Field

from .character_item import CharacterItem


class AnimeCharacter(BaseModel):
    character: CharacterItem | None = Field(None, description='Character details')
    role: str | None = Field(None, description="Character's Role")
    voice_actors: list[VoiceActor] | None = None


class AnimeCharacters(BaseModel):
    data: list[AnimeCharacter] | None = None
