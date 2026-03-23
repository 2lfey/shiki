from pydantic import BaseModel, Field


class Images(BaseModel):
    image_url: str | None = Field(None, description='Default Image Size URL (120x90)')
    small_image_url: str | None = Field(None, description='Small Image Size URL (640x480)')
    medium_image_url: str | None = Field(None, description='Medium Image Size URL (320x180)')
    large_image_url: str | None = Field(None, description='Large Image Size URL (480x360)')
    maximum_image_url: str | None = Field(None, description='Maximum Image Size URL (1280x720)')