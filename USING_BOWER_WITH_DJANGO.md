Using bower with Django
(see http://django-bower.readthedocs.org/en/latest/installation.html)

Installation
Install bower from npm:

npm install -g bower

And django-bower package:

pip install django-bower

Add django-bower to INSTALLED_APPS in your settings:

'djangobower',

Add staticfinder to STATICFILES_FINDERS:

'djangobower.finders.BowerFinder',

Specify path to components root (you need to use absolute path):

BOWER_COMPONENTS_ROOT = '/PROJECT_ROOT/mysite/'

If you need, you can manually set path to bower

BOWER_PATH = '/usr/bin/bower'

Example settings file with django-bower:

=======================================================================

import os


PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'

BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_ROOT, 'mysite')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

SECRET_KEY = 'g^i##va1ewa5d-rw-mevzvx2^udt63@!xu$-&di^19t)5rbm!5'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'example.urls'

WSGI_APPLICATION = 'example.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'djangobower',
)

BOWER_INSTALLED_APPS = (
    'jquery',
    'underscore',
)

=======================================================================

Download bower packages with management command:

./manage.py bower install


Add scripts in template, like:

{% load static %}
<script type="text/javascript" src='{% static 'jquery/dist/jquery.min.js' %}'></script>

In production you need to call bower install before collectstatic:

./manage.py bower install
./manage.py collectstatic

If you need to pass arguments to bower, like –allow-root, use:

./manage.py bower install -- --allow-root

You can use bower freeze to receive BOWER_INSTALLED_APPS with fixed current versions:

./manage.py bower freeze

You can call bower commands like info and update with:

./manage.py bower info backbone
./manage.py bower update


