From within the root directory ('django-frontend') type:

python manage.py makemigrations browse

The SQL generated for the migration can be viewed by typing (where 0001 is the number of the migration):

python manage.py sqlmigrate browse 0001

To check for any problems in your project without making migrations or touching the database.you can also run:
 
python manage.py check

Now, run migrate again to create those model tables in your database:

python manage.py migrate