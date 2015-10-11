To create the tables in the database (SQLite3), run the following command from the root of the repository:

python manage.py migrate

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app (we’ll cover those later). You’ll see a message for each migration it applies. If you’re interested, run the command-line client for your database and type 

\dt 					(PostgreSQL), 

mysql>SHOW TABLES; 		(MySQL), or 

sqlite>.schema 				(SQLite) 

to display the tables Django created.