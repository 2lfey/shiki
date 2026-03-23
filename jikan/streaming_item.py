from pydantic import BaseModel


class StreamingItem(BaseModel):
    name: str | None = None
    url: str | None = None