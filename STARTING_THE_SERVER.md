Let’s verify your Django project works. Change into the outer django-frontend directory, if you haven’t already, and run the following commands:

$ python manage.py runserver

You’ll see the following output on the command line:

Performing system checks...

0 errors found
August 12, 2015 - 15:50:53
Django version 1.8, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Or for the non-default port (8000) run the following command:

$ python manage.py runserver 8080

Now if you open your browser to the URL mentioned above, you should see:
_______________

It worked!
Congratulations on your first Django-powered page.

Of course, you haven't actually done any work yet. Next, start your first app by running python manage.py startapp [app_label].
You're seeing this message because you have DEBUG = True in your Django settings file and you haven't configured any URLs. Get to work!

_______________