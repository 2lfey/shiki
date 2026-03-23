from pydantic import BaseModel


class Theme(BaseModel):
    openings: list[str] | None = None
    endings: list[str] | None = None