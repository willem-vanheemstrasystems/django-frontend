from django.conf.urls import url
from mysite.client import views

urlpatterns = [
    url(r'^$', 'mysite.client.views.index', name='index'),
]
