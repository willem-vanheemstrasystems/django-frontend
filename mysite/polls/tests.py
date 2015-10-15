import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

# Create your tests here.

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        # create a Question instance with pub_date 30 days in the future
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        # was it published recently?
        self.assertEqual(future_question.was_published_recently(), False)
        
        
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        # create a Question instance with pub_date 1 day in the past
        time = timezone.now() - datetime.timedelta(days=1)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)
        
        
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        # create a Question instance with pub_date 23 hours in the past
        time = timezone.now() - datetime.timedelta(hours=23)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)
