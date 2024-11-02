FROM python:3.12-slim

WORKDIR /migrations

COPY poetry/migrations ./
COPY alembic.ini ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY app/pkg/models/ /migrations/app/pkg/models/
COPY app/config/ /migrations/app/config/
COPY migrations/ /migrations/migrations/
COPY .env ./
