FROM python:3.12-alpine

WORKDIR /api

COPY poetry/ ./
RUN apk update && \
    apk add --no-cache g++ musl-dev libffi-dev abseil-cpp

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . .
