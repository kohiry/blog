FROM python:3.12-slim

WORKDIR /migrations

COPY poetry/ ./
COPY alembic.ini ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --with sqlalchemy --without fastapi pydantic pydantic-settigns uvicorn apache-airflow  apache-airflow-providers-postgres google-re2 pep517

COPY app/pkg/models/ /migrations/app/pkg/models/
COPY app/config/ /migrations/app/config/
COPY migrations/ /migrations/migrations/
COPY .env ./
