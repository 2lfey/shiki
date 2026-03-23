from pydantic import BaseModel, Field


class CharacterPicture(BaseModel):
    image_url: str | None = Field(None, description='Default JPG Image Size URL')
    large_image_url: str | None = Field(None, description='Large JPG Image Size URL')


class CharacterPictures(BaseModel):
    data: list[CharacterPicture] | None = None