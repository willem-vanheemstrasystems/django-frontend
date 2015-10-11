PYTHON Django Notes:

[Using brew for Mac, run the following command frequently to check if there are any issue with the install: brew doctor]

To activate an environment that already exists, but is not active, type from outside of the environment folder (e.g. django-headstart) the following:

source django-headstart/bin/activate

Notice that the command prompt now starts with (django-headstart), like so:

(django-headstart)Macintosh-8:python wvanheemstra$

The environment 'django-headstart' is now active, it (may) contains projects which you can go into, like so:

cd django-headstart/bin/django_test

In here is where we edit the settings file, inside the sub-folder (django-headstart/bin/django_test/django_test):

cd django_test

settings.py

CREATING AN APP

To create an app (e.g. article) in our django_test project, from within the project folder (django-headstart/bin/diango_test) type:

python manage.py startapp article

NOTE: To check where the currently used version of python is installed on a Mac, type:
which python

You should get a reply, similar to:
/usr/bin/python

This is a symlink that points to your actual Python installation.
Next, type cd /usr/bin; ls -l python2.7, and the output should be something like:

lrwxr-xr-x  1 root  wheel  75 18 Feb  2014 python2.7 -> ../../System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7

NOTE: To check the version of python used, type:
./manage.py --version

The first change to make is to move /Library/Python/2.7/site-packages to the beginning of PYTHONPATH. Make these changes by adding two lines to your .profile file (which is in ~/):
The second is to set an alias so that python 2.7 is used.

export PYTHONPATH="/Library/Python/2.5/site-packages:$PYTHONPATH"
alias python=python2.5


To deactivate an environment, from within the environment type:

deactivate

Notice that the command prompt now no longer starts with (django-headstart), but like so:

Macintosh-8:python wvanheemstra$
