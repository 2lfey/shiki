from pydantic import BaseModel

from typing import Optional


class Studio(BaseModel):
    id: int
    name: str
    filtered_name: str
    real: bool
    image: Optional[str]