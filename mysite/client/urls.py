from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /client/
    url(r'^$', 'mysite.client.views.index', name='index'),
]
