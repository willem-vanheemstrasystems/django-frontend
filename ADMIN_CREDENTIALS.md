Creating an admin user¶

First we’ll need to create a user who can login to the admin site. Run the following command:

$ python manage.py createsuperuser

Enter your desired username and press enter.

Username: admin

You will then be prompted for your desired email address:

Email address: admin@mysite.com

The final step is to enter your password. You will be asked to enter your password (here: password) twice, the second time as a confirmation of the first.

Password: **********
Password (again): *********
Superuser created successfully.

For the sake of this example project the following admin credentials apply:

username:  admin
email:     admin@mysite.com
password:  password
role:      Superuser

You can login to the admin side by following:

http://127.0.0.1/admin/