from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', 'mysite.client.views.index', name='index'),
]
