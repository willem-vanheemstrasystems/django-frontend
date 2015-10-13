from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# All Django wants returned is an HttpResponse. Or an exception.

def index(request):
    # The code below loads the template called client/index.html
    # and passes it a context.
    # The context is a dictionary mapping template variable names to Python objects.
    context = {}
    # The render() function takes the request object as its first argument, 
    # a template name as its second argument 
    # and a dictionary as its optional third argument. 
    # It returns an HttpResponse object of the given template rendered with the given context.
    return render(request, 'client/index.html', context)