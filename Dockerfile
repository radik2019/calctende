FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

WORKDIR /calctende_app

COPY . /calctende_app/

RUN apt-get update 
RUN apt-get install -y postgresql-client
RUN apt-get install redis

RUN pip install --upgrade pip
RUN pip install -r /calctende_app/requirements.txt

RUN python manage.py collectstatic
