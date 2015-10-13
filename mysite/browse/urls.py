from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', 'mysite.browse.views.index', name='index'),
]
