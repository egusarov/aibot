from app.celery_app import celery_app
import logging

logger = logging.getLogger(__name__)


@celery_app.task
def fetch_news():
    logger.warning("FETCH NEWS TASK WORKS")
