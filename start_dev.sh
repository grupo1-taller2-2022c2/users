#!/bin/bash

set -e

# Si hay problemas porque algún proceso está usando un puerto, se puede hacer 
# sudo netstat -ano -p tcp | grep <puerto>
# y agarrás el PID y le haces
# sudo kill -9 pid

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

docker-compose up -d $DB_SERVICE_NAME 
sleep 3

if [[ $1 = "rebuild" ]];
then
    echo "Rebuilding images..."
    docker-compose up --build -d $FRONTEND_SERVICE_NAME
    docker-compose up --build -d $BACKEND_SERVICE_NAME
else
    docker-compose up -d $FRONTEND_SERVICE_NAME
    sleep 2
    docker-compose up -d $BACKEND_SERVICE_NAME
fi

sleep 3
echo "Entering bash console for users backend..."
docker-compose exec $BACKEND_SERVICE_NAME /bin/bash
# alembic upgrade head
