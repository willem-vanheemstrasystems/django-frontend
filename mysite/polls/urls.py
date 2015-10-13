from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    # The 'name' value as called by the {% url 'index' %} template tag
    url(r'^$', 'mysite.polls.views.index', name='index'),
    # ex: /polls/5/
    # Django will have stripped off the matching text ("polls/") 
    # and send the remaining text - "5/" - to this 'polls.urls' URLconf 
    # for further processing which matches r'^(?P<question_id>[0-9]+)/$' 
    # resulting in a call to the detail() view like so:
    #    detail(request=<HttpRequest object>, question_id='5')
    # The question_id='5' part comes from (?P<question_id>[0-9]+). 
    # Using parentheses around a pattern "captures" the text matched by that pattern 
    # and sends it as an argument to the view function; 
    # ?P<question_id> defines the name that will be used to identify the matched pattern; 
    # and [0-9]+ is a regular expression to match a sequence of digits (i.e., a number).
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
