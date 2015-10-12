from django.conf.urls import url
from mysite.browse import views

urlpatterns = [
    url(r'^$', 'mysite.browse.views.index', name='index'),
]
