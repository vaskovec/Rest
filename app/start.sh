#!/bin/bash

sleep 1

if [ $DJANGO_DEBUG = "true" ]; then
    echo "[START] install dependencies"
    pip install -r requirements.txt
fi

if [ $MIGRATIONS = "true" ]; then
    echo "[START] apply migrations"
    python manage.py migrate
fi

if [ $DJANGO_DEBUG = "true" ]; then
    echo "[START] launch app in DEBUG mode"
    python manage.py runserver 0.0.0.0:8000
else
    python manage.py collectstatic --noinput
    echo "[START] launch app in RELEASE mode"
    uwsgi --chdir=. \
          --module=secret_santa.wsgi:application \
          --env DJANGO_SETTINGS_MODULE=secret_santa.settings \
          --master \
          --http=0.0.0.0:8000 \
          --processes=3 \
          --buffer-size=32768 \
          --threads=4 \
          --uid=1000 --gid=2000 \
          --harakiri=300 \
          --max-requests=5000 \
          --vacuum
fi