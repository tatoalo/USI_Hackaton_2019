FROM python:3.8.0-buster

WORKDIR /app

COPY backend/requirements.txt /app

RUN pip install -r requirements.txt

COPY ./backend /app