from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.

# All Django wants returned is an HttpResponse. Or an exception.
'''
file views
'''

def index(request):
    return render(request, 'mysite/index.html')