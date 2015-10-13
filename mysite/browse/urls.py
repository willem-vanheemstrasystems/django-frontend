from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /browse/
    url(r'^$', 'mysite.browse.views.index', name='index'),
]

