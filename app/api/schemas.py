from pydantic import BaseModel

class SourceCreate(BaseModel):
    type: str
    name: str
    url: str


class KeywordCreate(BaseModel):
    word: str
