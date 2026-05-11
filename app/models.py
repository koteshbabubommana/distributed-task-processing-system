from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskRequest(BaseModel):
    task_name: str
    payload: Optional[dict] = None
    priority: Optional[str] = "normal"


class TaskResponse(BaseModel):
    task_id: str
    status: str
    created_at: datetime
    message: str


class HealthResponse(BaseModel):
    service: str
    status: str