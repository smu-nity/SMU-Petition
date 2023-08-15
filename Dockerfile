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
RUN apt-get update
RUN apt-get -y install cron
ADD scripts/crontab-script /etc/cron.d/task-cron
RUN chmod 0644 /etc/cron.d/task-cron
CMD start.sh
