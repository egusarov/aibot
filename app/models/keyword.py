import uuid

from app.db.base import Base
from sqlalchemy import String, Column


class Keyword(Base):
    __tablename__ = "keywords"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    word = Column(String, unique=True)
