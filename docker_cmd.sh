#!/bin/bash

service cron start
python manage.py crontab add
gunicorn config.wsgi:application --bind 0.0.0.0:8000
