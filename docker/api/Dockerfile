FROM python:3.12-alpine

WORKDIR /api
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .