from pydantic import BaseModel

from typing import Optional


class Image(BaseModel):
    original: Optional[str]
    preview: Optional[str]