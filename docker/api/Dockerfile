FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y g++ libffi-dev && \
    apt-get clean


WORKDIR /api

COPY poetry/ ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only api

COPY . .
