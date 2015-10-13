from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question

# Create your views here.

# All Django wants returned is an HttpResponse. Or an exception.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # The code below loads the template called polls/index.html
    # and passes it a context.
    # The context is a dictionary mapping template variable names to Python objects.
    context = {'latest_question_list': latest_question_list}
    # The render() function takes the request object as its first argument, 
    # a template name as its second argument 
    # and a dictionary as its optional third argument. 
    # It returns an HttpResponse object of the given template rendered with the given context.
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # The get_object_or_404() function takes a Django model as its first argument 
    # and an arbitrary number of keyword arguments, 
    # which it passes to the get() function of the model's manager. 
    # It raises Http404 if the object doesn't exist.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)