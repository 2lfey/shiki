from pydantic import BaseModel, Field

from .user_images import UserImages


class UserMeta(BaseModel):
    username: str | None = Field(None, description='MyAnimeList Username')
    url: str | None = Field(None, description='MyAnimeList Profile URL')
    images: UserImages | None = None