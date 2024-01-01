FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

WORKDIR /calctende_app

COPY . /calctende_app/

RUN apt-get update && apt-get install -y libpq-dev 
RUN apt-get install -y postgresql-client
RUN apt-get install redis -y

RUN pip install --upgrade pip
RUN pip install -r /calctende_app/requirements.txt

RUN python manage.py collectstatic
