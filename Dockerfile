FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

COPY ./app /root/app
COPY ./alembic /root/alembic
COPY ./alembic.ini /root/

RUN apt-get -y update

RUN apt-get -y install \
  dos2unix \
  libpq-dev \
  libmariadb-dev-compat \
  libmariadb-dev \
  alembic \
  gcc \
  && apt-get clean

COPY ./requirements.txt /root/requirements.txt
COPY ./tests /root/tests
COPY ./run_tests.sh /root/

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt