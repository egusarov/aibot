from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class Source(Base):
    __tablename__ = "sources"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    type = Column(String)
    name = Column(String)
    url = Column(String)
    enabled = Column(Boolean, default=True)


class Keyword(Base):
    __tablename__ = "keywords"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    word = Column(String, unique=True)
