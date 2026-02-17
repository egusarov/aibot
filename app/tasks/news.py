from app.celery_app import celery_app
import logging

logger = logging.getLogger(__name__)


@celery_app.task(name="app.tasks.news.fetch_news")
def fetch_news():
    logger.info("Fetching news...")
