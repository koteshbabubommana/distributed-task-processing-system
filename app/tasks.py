import time
import random
from app.task_queue import celery_app
from app.utils.logger import logger


@celery_app.task(
    bind=True,
    max_retries=3,
    default_retry_delay=5,
    name="process_distributed_task",
)
def process_distributed_task(self, task_name: str, payload: dict | None = None):
    try:
        logger.info(f"Task started | task_name={task_name} | task_id={self.request.id}")

        start_time = time.time()

        time.sleep(random.randint(2, 5))

        if task_name.lower() == "fail":
            raise ValueError("Simulated task failure for retry testing")

        processing_time = round(time.time() - start_time, 2)

        result = {
            "task_id": self.request.id,
            "task_name": task_name,
            "status": "completed",
            "payload": payload or {},
            "processing_time_seconds": processing_time,
        }

        logger.info(f"Task completed | task_id={self.request.id}")

        return result

    except Exception as exc:
        logger.error(f"Task failed | task_id={self.request.id} | error={str(exc)}")
        raise self.retry(exc=exc)