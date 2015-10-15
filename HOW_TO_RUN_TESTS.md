How to run tests
(see https://docs.djangoproject.com/en/1.8/intro/tutorial05/)

A conventional place for an application’s tests is in the application’s tests.py file; the testing system will automatically find tests in any file whose name begins with test.

To run a test in the 'mysite' subdirectory, from the root directory ('django-frontend') that has the file manage.py in it, run:

python manage.py test mysite

or at an application level:

python manage.py test mysite.polls

It will run all files that have the word 'test' as the start of the file name.

NOTE: Best Practise is to always use ./manage.py shell instead of starting Python directly. It will set up the environment for you.


The Django test client¶

Django provides a test Client to simulate a user interacting with the code at the view level. We can use it in tests.py or even in the shell.

We will start again with the shell, where we need to do a couple of things that won’t be necessary in tests.py. The first is to set up the test environment in the shell:

>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()

setup_test_environment() installs a template renderer which will allow us to examine some additional attributes on responses such as response.context that otherwise wouldn't be available. Note that this method does not setup a test database, so the following will be run against the existing database and the output may differ slightly depending on what questions you already created.

Next we need to import the test client class (later in tests.py we will use the django.test.TestCase class, which comes with its own client, so this won’t be required):

>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()

With that ready, we can ask the client to do some work for us:

>>> # get a response from '/doesnotexist'
>>> response = client.get('/doesnotexist')
>>> # we should expect a 404 from that address
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.core.urlresolvers import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
200
>>> response.content
'\n\n\n    <p>No polls are available.</p>\n\n'
>>> # note - you might get unexpected results if your ``TIME_ZONE``
>>> # in ``settings.py`` is not correct. If you need to change it,
>>> # you will also need to restart your shell session
>>> from mysite.polls.models import Question
>>> from django.utils import timezone
>>> # create a Question and save it
>>> q = Question(question_text="Who is your favorite Beatle?", pub_date=timezone.now())
>>> q.save()
>>> # check the response once again
>>> response = client.get('/polls/')
>>> response.content
'\n\n\n    <ul>\n    \n        <li><a href="/polls/1/">Who is your favorite Beatle?</a></li>\n    \n    </ul>\n\n'
>>> # If the following doesn't work, you probably omitted the call to
>>> # setup_test_environment() described above
>>> response.context['latest_question_list']
[<Question: Who is your favorite Beatle?>]


Further testing

You can use an “in-browser” framework such as Selenium to test the way your HTML actually renders in a browser. These tools allow you to check not just the behavior of your Django code, but also, for example, of your JavaScript. 

It’s quite something to see the tests launch a browser, and start interacting with your site, as if a human being were driving it! Django includes LiveServerTestCase to facilitate integration with tools like Selenium.

If you have a complex application, you may want to run tests automatically with every commit for the purposes of continuous integration, so that quality control is itself - at least partially - automated.

A good way to spot untested parts of your application is to check code coverage. This also helps identify fragile or even dead code. If you can’t test a piece of code, it usually means that code should be refactored or removed. Coverage will help to identify dead code. See Integration with coverage.py for details.
