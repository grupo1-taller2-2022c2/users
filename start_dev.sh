#!/bin/bash

set -e

BACKEND_CONTAINER_NAME="users-backend-container"
FRONTEND_CONTAINER_NAME="backoffice-frontend-container"
DB_CONTAINER_NAME="postgres-container"

BACKEND_SERVICE_NAME="users_backend"
FRONTEND_SERVICE_NAME="backoffice_frontend"
DB_SERVICE_NAME="dev_db"

echo "Deleting containers if exist..."
{ docker ps -q -f name=$BACKEND_CONTAINER_NAME | xargs docker stop | xargs docker rm; } 2>> /dev/null || echo
{ docker ps -q -f name=$FRONTEND_CONTAINER_NAME | xargs docker stop | xargs docker rm; } 2>> /dev/null || echo
{ docker ps -q -f name=$DB_CONTAINER_NAME | xargs docker stop | xargs docker rm; } 2>> /dev/null || echo

docker-compose up --force-recreate -d $BACKEND_SERVICE_NAME 
sleep 3
docker-compose up --force-recreate --build -d $BACKEND_SERVICE_NAME
docker-compose up --force-recreate --build -d $FRONTEND_SERVICE_NAME
