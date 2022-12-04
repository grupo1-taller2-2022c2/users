#!/bin/bash
# Run migrations and launch app (entrypoint used for prod and test)
alembic upgrade head
uvicorn "app.main:app" --host 0.0.0.0 --port=${PORT:-5000}