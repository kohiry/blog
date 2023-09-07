FROM python:alpine

WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY pyproject.toml .

RUN pip install poetry && poetry config virtualenvs.create false --local
RUN poetry install

COPY . .
