# Distributed Task Processing & Monitoring Platform

A production-style distributed backend platform for asynchronous task execution, queue orchestration, retry handling, worker monitoring, and scalable backend processing using FastAPI, Celery, Redis, and Docker.

## Architecture

```text
Client / API User
      ↓
FastAPI Backend
      ↓
Redis Task Queue
      ↓
Celery Worker
      ↓
Task Execution
      ↓
Task Status + Metrics
```

## Tech Stack

- Python
- FastAPI
- Celery
- Redis
- Docker
- Docker Compose
- Uvicorn
- Pytest

## Features

- Asynchronous task processing
- Distributed worker orchestration
- Redis-backed queue system
- Retry handling for failed tasks
- Task status tracking
- Health check endpoint
- Metrics endpoint
- Dockerized multi-service setup
- Swagger API documentation
- Structured project layout

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Home endpoint |
| GET | `/health` | Service health check |
| POST | `/tasks` | Submit a new async task |
| GET | `/tasks/{task_id}` | Check task execution status |
| GET | `/metrics` | View queue and worker metrics |

## Run Instructions

### 1. Clone the repository

```bash
git clone https://github.com/koteshbabubommana/distributed-task-processing-system.git
cd distributed-task-processing-system
```

### 2. Run with Docker

```bash
docker compose up --build
```

### 3. Open Swagger API Docs

```text
http://localhost:8000/docs
```

### 4. Submit a sample task

Use `POST /tasks` with this request body:

```json
{
  "task_name": "image_processing_task",
  "payload": {
    "file": "image1.png"
  },
  "priority": "high"
}
```

### 5. Check task status

Copy the returned `task_id` and use:

```text
GET /tasks/{task_id}
```

## Project Structure

```text
distributed-task-processing-system/
├── app/
│   ├── utils/
│   │   └── logger.py
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── monitoring.py
│   ├── task_queue.py
│   ├── tasks.py
│   └── worker.py
├── tests/
│   └── test_tasks.py
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
└── requirements.txt
```

## Monitoring

The project includes basic monitoring support through:

- `/health` endpoint
- `/metrics` endpoint
- Celery worker logs
- Redis queue visibility
- Docker container logs

## Future Enhancements

- Prometheus metrics
- Grafana dashboard
- PostgreSQL task history storage
- JWT authentication
- Rate limiting
- Kubernetes deployment
- GitHub Actions CI/CD
- Cloud deployment on Render, Railway, AWS, or GCP

## Author

Kotesh Babu Bommana