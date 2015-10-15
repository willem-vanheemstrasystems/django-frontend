Playing with the API¶
(see https://docs.djangoproject.com/en/1.8/intro/tutorial01/)

Now, let’s hop into the interactive Python shell and play around with the free API Django gives you. To invoke the Python shell, use this command:

python manage.py shell

The prompt now will start with >>>

Now you can do something like:

>>> import datetime
>>> from django.utils import timezone
>>> from mysite.polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # was it published recently?
>>> future_question.was_published_recently()

To exit the >>> type 

>>> exit() <RETURN>

