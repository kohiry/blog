FROM python:3.11-slim

WORKDIR /api

COPY poetry/ ./
RUN apk update && \
    apk add --no-cache g++ musl-dev libffi-dev

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . .
