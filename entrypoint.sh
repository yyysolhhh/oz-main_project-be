#!/bin/sh

ln -sf prod.py config/settings/settings.py
#sudo apt-get update
#sudo apt-get install vim -y
export DJANGO_SETTINGS_MODULE=config.settings.settings

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py shell < tools/create_superuser.py
#python manage.py runserver 0.0.0.0:80

gunicorn --bind 0:8000 config.wsgi:application
#uvicorn config.asgi:application --port 80 --workers 4
