FROM python:3.13-slim

WORKDIR /parking_service

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN playwright install chromium
RUN playwright install-deps chromium

COPY . .

EXPOSE 8000
