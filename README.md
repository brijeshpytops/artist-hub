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
- Extension for sqlite3: SQLite Viewer - Florian Klampfer
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

- create django application
([venv-name]).../artist-hub>>> mkdir [apps-dir-name]
Example : AHApps
            - master
            - web....
[apps-dir-name]/app1
[apps-dir-name]/app2
([venv-name]).../artist-hub>>> python manage.py startapp [app-name] [apps-dir-name]/[app-name]

Go to the project/sttings.py/
install your app's in settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '[apps-dir-name].app1',
    '[apps-dir-name].app2'
]

- Setup Templates&Static files
[apps-dir-name]/app1
    - templates
        - app1
    - static
        - CSS
            - styles.css
        - JS
            - index.js
        - Fonts
            - google-fonts
        - images
            - logo.png

- setup STATIC/MEDIA path in settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

Go to project/urls.py
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


([venv-name]).../artist-hub>>> python manage.py collectstatic


Remove something from Git Cache 
>>> git rm -r --cached path/to/your-directory/


Form setup: 

1] form tag inside attribute must be:
action="" method="post" enctype="multipart/form-data"[if file field is there]

2] {% csrf_token %}

3] inside input field must be required "name" attribute

4] btn type must be submit
