from django.conf.urls import url
from mysite.polls import views

urlpatterns = [
    url(r'^$', 'mysite.polls.views.index', name='index'),
]
