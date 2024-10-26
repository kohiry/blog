FROM python:3.12-alpine

WORKDIR /api

COPY poetry/ ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . .