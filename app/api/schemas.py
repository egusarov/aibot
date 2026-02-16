from pydantic import BaseModel
from typing import Optional
from uuid import UUID


# -------- SOURCES --------

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


# -------- KEYWORDS --------

class KeywordCreate(BaseModel):
    word: str


class KeywordOut(BaseModel):
    id: str
    word: str

    class Config:
        from_attributes = True
