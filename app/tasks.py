from app.celery_app import celery_app
import time

@celery_app.task(bind=True)
def debug_task(self):
    time.sleep(2)
    return {
        "task_id": self.request.id,
        "status": "ok"
    }
