FROM python:alpine

WORKDIR /app

COPY pyproject.toml .

RUN pip install poetry && poetry config virtualenvs.create false --local
RUN poetry install

COPY . .
