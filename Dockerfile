FROM python:3.10.2-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install pipenv

COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
