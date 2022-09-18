#!/bin/bash

set -e

docker-compose up -d dev_db
sleep 3
docker-compose up users_backend
#docker-compose exec users_backend /bin/bash
