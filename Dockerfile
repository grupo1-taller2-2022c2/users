FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

COPY ./app /app/app
COPY ./alembic /app/alembic
COPY ./alembic.ini /app/

RUN apt-get -y update

RUN apt-get -y install \
  dos2unix \
  libpq-dev \
  libmariadb-dev-compat \
  libmariadb-dev \
  alembic \
  gcc \
  && apt-get clean

COPY ./requirements.txt /app/requirements.txt
COPY ./tests /app/tests
COPY ./run_tests.sh /app/

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt