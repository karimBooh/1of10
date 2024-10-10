from datetime import datetime

from pydantic import BaseModel

class ThumbnailFeedback(BaseModel):
    image: bytes

class ThumbnailBase(BaseModel):
    image: bytes
    feedback: str

class ThumbnailCreate(ThumbnailBase):
    image: bytes
    feedback: str


class Thumbnail(ThumbnailBase):
    id: int
    creation_date: datetime
    update_date: datetime

    class Config:
        orm_model = True