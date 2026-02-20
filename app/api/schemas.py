from pydantic import BaseModel
from datetime import datetime


class SourceBase(BaseModel):
    type: str
    name: str
    url: str
    enabled: bool = True


class SourceCreate(SourceBase):
    pass


class SourceOut(SourceBase):
    id: str

    class Config:
        from_attributes = True


class KeywordCreate(BaseModel):
    word: str


class KeywordOut(BaseModel):
    id: str
    word: str

    class Config:
        from_attributes = True


class NewsOut(BaseModel):
    id: int
    source: str
    title: str
    url: str
    content: str | None
    published_at: datetime | None
    created_at: datetime

    class Config:
        from_attributes = True
