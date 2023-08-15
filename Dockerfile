# pull official base image
FROM python:3.9-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app/
# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# for django-crontab
RUN chmod -R 777 /usr/src/app
RUN apt-get update
RUN apt-get install -y cron && touch /usr/src/app/cron.log
RUN service cron start
RUN python manage.py crontab add
