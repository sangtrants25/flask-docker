#!/bin/sh
echo "! Waiting for postgres..."

while ! nc -z user-db 5432; do
  sleep 0.1
done

# flask run -h 0.0.0.0

gunicorn -c ./gunicorn.config.py manage