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

# Time Setting (KST)
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y tzdata
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

# for django-crontab
RUN apt-get update
RUN apt-get -y install cron
RUN apt-get -y install vim
