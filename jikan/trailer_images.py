from pydantic import BaseModel

from .images import Images


class TrailerImages(BaseModel):
    images: Images | None = None