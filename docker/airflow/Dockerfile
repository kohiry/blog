FROM apache/airflow:2.7.2

COPY poetry/airflow ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

