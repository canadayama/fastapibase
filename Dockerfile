FROM python:3.11-slim

ENV LANG=C.UTF-8

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

# To build psycopg2
RUN apt-get install -y build-essential libpq-dev python3-dev postgresql-server-dev-all

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install --no-cache -r requirements.txt
