#!/bin/bash


# Install requirements

pip install --upgrade pip
pip install -r requirements.txt


# Create and populate the .env file
cat <<EOL > .env
SECRET_KEY='django-insecure-kh3afnr1^%bi41&ln3(hir(fo#vu9c11e5i&f4936kw)3-27-%'
DEBUG=True
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=database

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='ghzlnghaya@gmail.com'
EMAIL_HOST_PASSWORD='mfqy gvma pglp nigl'
EOL

# Change permissions of the .env file
chmod 755 .env

# Start Docker containers
docker-compose down
docker-compose up -d

# Run migrations and start the server
python manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py runserver













#---------------------------------------------------


# python3 -m venv ../myenv
# docker-compose up -d
# source ../myenv/bin/activate
# pip install -r requirements.txt
# touch ../.env
