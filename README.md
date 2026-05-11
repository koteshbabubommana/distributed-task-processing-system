# Distributed Task Processing & Monitoring Platform

A production-style distributed backend platform for asynchronous task execution, queue orchestration, retry handling, worker monitoring, and scalable backend processing using FastAPI, Celery, Redis, and Docker.

---

## Features

- Asynchronous task processing
- Distributed worker orchestration
- Queue-based architecture
- Retry mechanisms for failed tasks
- Redis-backed task broker
- Dockerized backend services
- REST API endpoints with FastAPI
- Task monitoring and status tracking
- Health check APIs
- Metrics endpoint for observability
- Structured logging support
- Scalable backend infrastructure

---

## Tech Stack

- Python
- FastAPI
- Celery
- Redis
- Docker
- Docker Compose
- Uvicorn
- Pytest

---

## Project Structure

```bash
distributed-task-processing-system/
│
├── app/
│   ├── main.py
│   ├── tasks.py
│   ├── worker.py
│   ├── task_queue.py
│   ├── monitoring.py
│   ├── models.py
│   ├── utils/
│   │   └── logger.py
│   └── __init__.py
│
├── tests/
│   └── test_tasks.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Home endpoint |
| GET | /health | Health check |
| POST | /tasks | Submit async task |
| GET | /tasks/{task_id} | Get task status |
| GET | /metrics | Monitoring metrics |

---

## Running Locally

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start application

```bash
python -m uvicorn app.main:app --reload
```

### Run with Docker

```bash
docker compose up --build
```

---

## Monitoring

The platform includes:
- worker monitoring
- queue depth visibility
- health checks
- metrics endpoint
- structured logging
- retry tracking

---

## Sample Task Request

```json
{
  "task_name": "image_processing_task",
  "payload": {
    "file": "image1.png"
  },
  "priority": "high"
}
```

---

## Future Enhancements

- Prometheus integration
- Grafana dashboards
- Kubernetes deployment
- RabbitMQ support
- Authentication & authorization
- Rate limiting
- CI/CD pipelines
- Auto-scaling workers

---

## Author

Kotesh Babu Bommana