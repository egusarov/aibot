from app.celery_app import celery_app

app = celery_app

celery_app.autodiscover_tasks(["app.tasks"])
