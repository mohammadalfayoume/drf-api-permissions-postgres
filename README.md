# Lab 26: Permissions & Postgresql

# Author: Mohammad Alfayoume

## Username and Password

1. superuser: username: admin , password: admin1234

2. staff: username: islam , password: asdfg1234

3. user: username: abed , password: asdfg1234

## runserver

`docker-compose up --build`

## create superuser
`docker-compose run web python manage.py createsuperuser`

## makemigrations
`docker-compose run web python manage.py makemigrations`

## migrate
`docker-compose run web python manage.py migrate`

## Test
`docker-compose run web python manage.py test`

