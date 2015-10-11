How to run tests

To run a test in the 'mysite' subdirectory, from the root directory ('django-frontend') that has the file manage.py in it, run:

python manage.py test mysite

It will run all files that have the word 'test' as the start of the file name.

NOTE: Best Practise is to always use ./manage.py shell instead of starting Python directly. It will set up the environment for you.