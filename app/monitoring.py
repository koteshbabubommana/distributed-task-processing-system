import os
import redis


REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")


def get_queue_metrics():
    redis_client = redis.Redis.from_url(REDIS_URL)

    return {
        "queue_name": "celery",
        "pending_tasks": redis_client.llen("celery"),
        "redis_status": "connected"
    }