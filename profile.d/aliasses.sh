#!/bin/bash

alias runserver="poetry run python /app/manage.py runserver 0.0.0.0:8000"
alias makemigrations="poetry run python /app/manage.py makemigrations"
alias migrate="poetry run python /app/manage.py migrate"
alias createsuperuser="poetry run python /app/manage.py createsuperuser"
alias shell="poetry run python /app/manage.py shell"
alias startapp="poetry run django-admin.py startapp"
