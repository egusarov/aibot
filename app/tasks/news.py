import logging
from datetime import datetime

from app.celery_app import celery_app
from app.db import SessionLocal
from app.models.news import NewsItem

logger = logging.getLogger(__name__)


@celery_app.task(name="app.tasks.news.fetch_news")
def fetch_news():
    db = SessionLocal()
    try:
        news = NewsItem(
            source="demo",
            title=f"Demo news at {datetime.utcnow().isoformat()}",
            url=f"https://example.com/{datetime.utcnow().timestamp()}",
            content="Test content",
            published_at=datetime.utcnow(),
        )

        db.add(news)
        db.commit()

        logger.warning("NewsItem saved to DB")
        return news.id

    finally:
        db.close()


from app.db.base import Base
print("Base id in news:", id(Base))