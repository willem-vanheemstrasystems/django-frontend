import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Question

# Create your tests here.

# A question shortcut function, to take some repetition out of the process of creating questions.
def create_question(question_text, days):
    """
    Creates a question with the given `question_text` published the given
    number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)
    
    
class QuestionMethodTests(TestCase):
    """
    class QuestionMethodTests(TestCase)
    """
    # test_index_view_with_no_questions doesn't create any questions, 
    # but checks the message: "No polls are available." and verifies the latest_question_list is empty. 
    # Note that the django.test.TestCase class provides some additional assertion methods. 
    # In these examples, we use assertContains() and assertQuerysetEqual().
    # The database is reset for each test method, so the first question is no longer there, 
    # and so again the index shouldn't have any questions in it.
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
        
        
    # In test_index_view_with_a_past_question, we create a question and verify that it appears in the list.
    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date 30 days in the past should be displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )
        
        
    # In test_index_view_with_a_future_question, we create a question with a pub_date in the future. 
    # The database is reset for each test method, so the first question is no longer there, 
    # and so again the index shouldn't have any questions in it.
    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date 1 day in the future should not be displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=1)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.",
                            status_code=200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
        
        
    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=1)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )
        
        
    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
        
        
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
