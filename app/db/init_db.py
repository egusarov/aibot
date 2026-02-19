from app.db.engine import engine
from app.db.base import Base

from app.models.news import NewsItem  # noqa: F401


def init_db():
    Base.metadata.create_all(bind=engine)
