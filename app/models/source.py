from app.db.base import Base
from sqlalchemy import String, Column, Boolean


class Source(Base):
    __tablename__ = "sources"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    type = Column(String)
    name = Column(String)
    url = Column(String)
    enabled = Column(Boolean, default=True)
