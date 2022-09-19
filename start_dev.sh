#!/bin/bash

set -e

docker-compose up --force-recreate -d dev_db 
sleep 3
docker-compose up --force-recreate users_backend 
docker-compose exec users_backend /bin/bash
