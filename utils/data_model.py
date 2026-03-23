from pydantic import BaseModel


class DataModel[T](BaseModel):
    data: T