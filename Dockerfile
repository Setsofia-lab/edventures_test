FROM python:3.9-alpine3.13
LABEL maintainer="setsofiaeli@gmail.com" 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/
