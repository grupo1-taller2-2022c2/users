#!/bin/bash

BACKEND_SERVICE_NAME="users_backend"

docker-compose up -d --build $BACKEND_SERVICE_NAME

echo "Ready. You can know run ./start_dev.sh to lift all containers..."