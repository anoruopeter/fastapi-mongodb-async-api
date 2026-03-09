# FastAPI MongoDB Async API

This project is a backend REST API built with FastAPI and MongoDB using an async architecture.

## Features

- Create logs
- Retrieve logs
- Retrieve a log by ID
- Update logs (PUT)
- Partial update (PATCH)
- Delete logs
- Pagination support (`/logs?limit=5`)
- Filtering (`/logs?level=ERROR`)
- Request logging middleware
- Health check endpoint (`/health`)

## Tech Stack

- FastAPI
- Python
- MongoDB
- Motor (async MongoDB driver)
- Docker
- Docker Compose

## Run locally

Activate environment:

venv\Scripts\activate


START API:

uvicorn app.main:app --reload


API docs:
http://127.0.0.1:8000/docs


## Run with Docker

docker compose up --build

## Example API calls

Get logs

GET /logs

Pagination

GET /logs?limit=10

Filter by level

GET /logs?level=ERROR

Health check

GET /health


