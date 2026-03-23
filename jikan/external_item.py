from pydantic import BaseModel


class ExternalItem(BaseModel):
    name: str | None = None
    url: str | None = None