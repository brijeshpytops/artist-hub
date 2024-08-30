# artist-hub

- create you repo on github and clone in local
(specific-location)>>> git clone https://github.com/brijeshpytops/artist-hub.git
(specific-location)>>> cd artist-hub

- make sure you alrady have installed python in your local system
.../artist-hub>>> python --version
Python 3.12.5

- create requirements.txt file in base dir
.../artist-hub>>> type nul > requirements.txt

- create virtual environments
.../artist-hub>>> python -m venv [venv-name]

- activate/deactivate your virtual env.
.../artist-hub>>> [venv-name]\Scripts\activate
([venv-name]).../artist-hub>>> [venv-name]\Scripts\deactivate

- checke installed modules and packages in vitrual env.
([venv-name]).../artist-hub>>> pip list\pip freeze

- install modules and packages 
([venv-name]).../artist-hub>>> pip install [module-name]==X.0.1

- install django
([venv-name]).../artist-hub>>> pip install django

- add installed modules and packages in requirements.txt
([venv-name]).../artist-hub>>> pip freeze > requirements.txt

- install/update modules and packages from requirements.txt
([venv-name]).../artist-hub>>> pip install -r requirements.txt

- make sure you have already installed django
([venv-name]).../artist-hub>>> python/ python -m django --version
Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.get_version()
'5.1'
>>> exit()

- Creating a project
([venv-name]).../artist-hub>>> django-admin startproject [project-name] .

- run local server
([venv-name]).../artist-hub>>> python manage.py runserver [port-number]

- migrate and makemigrations of database model's
([venv-name]).../artist-hub>>> python manage.py makemigrations
([venv-name]).../artist-hub>>> python manage.py migrate

- create super user
([venv-name]).../artist-hub>>> python manage.py createsuperuser
Username (leave blank to use 'tops'): admin
Email address: admin@gmail.com
Password: ********
Password (again): ********
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.