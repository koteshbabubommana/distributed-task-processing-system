from datetime import datetime
from fastapi import FastAPI
from celery.result import AsyncResult

from app.models import TaskRequest, TaskResponse, HealthResponse
from app.tasks import process_distributed_task
from app.task_queue import celery_app
from app.monitoring import get_queue_metrics


app = FastAPI(
    title="Distributed Task Processing & Monitoring Platform",
    description="A production-style backend platform for asynchronous task execution, retries, queue monitoring, and worker orchestration.",
    version="1.0.0",
)


@app.get("/", response_model=HealthResponse)
def home():
    return {
        "service": "Distributed Task Processing Platform",
        "status": "running",
    }


@app.get("/health", response_model=HealthResponse)
def health_check():
    return {
        "service": "Distributed Task Processing Platform",
        "status": "healthy",
    }


@app.post("/tasks", response_model=TaskResponse)
def submit_task(request: TaskRequest):
    task = process_distributed_task.delay(
        request.task_name,
        request.payload,
    )

    return {
        "task_id": task.id,
        "status": "queued",
        "created_at": datetime.utcnow(),
        "message": "Task submitted successfully",
    }


@app.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)

    response = {
        "task_id": task_id,
        "status": task_result.status,
    }

    if task_result.ready():
        response["result"] = task_result.result

    return response


@app.get("/metrics")
def metrics():
    return get_queue_metrics()