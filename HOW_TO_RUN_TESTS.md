How to run tests
(see https://docs.djangoproject.com/en/1.8/intro/tutorial05/)

A conventional place for an application’s tests is in the application’s tests.py file; the testing system will automatically find tests in any file whose name begins with test.

To run a test in the 'mysite' subdirectory, from the root directory ('django-frontend') that has the file manage.py in it, run:

python manage.py test mysite

or at an application level:

python manage.py test mysite.polls

It will run all files that have the word 'test' as the start of the file name.

NOTE: Best Practise is to always use ./manage.py shell instead of starting Python directly. It will set up the environment for you.