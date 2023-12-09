FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

WORKDIR /calctende_app

COPY . /calctende_app/

RUN apt-get update && \
    apt-get install -y postgresql-client

RUN pip install --upgrade pip
RUN pip install -r /calctende_app/requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
