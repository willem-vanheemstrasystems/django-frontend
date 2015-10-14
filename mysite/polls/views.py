from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Choice, Question

# Create your views here.

# All Django wants returned is an HttpResponse. Or an exception.
'''
file views
'''


def index(request):
    '''
    function index(request)
    '''
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
    '''
    function detail(request, question_id)
    '''
    # The get_object_or_404() function takes a Django model as its first argument 
    # and an arbitrary number of keyword arguments, 
    # which it passes to the get() function of the model's manager. 
    # It raises Http404 if the object doesn't exist.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    '''
    function results(request, question_id)
    '''
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    '''
    function vote(request, question_id)
    '''
    #return HttpResponse("You're voting on question %s." % question_id)
    p = get_object_or_404(Question, pk=question_id)
    # request.POST is a dictionary-like object that lets you access submitted data by key name. 
    # In this case, request.POST['choice'] returns the ID of the selected choice, as a string. 
    # request.POST values are always strings.
    #
    # Note that Django also provides request.GET for accessing GET data in the same way - but 
    # we're explicitly using request.POST in our code, to ensure that data is only altered via a POST call.
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # request.POST['choice'] will raise KeyError if choice wasn't provided in POST data. 
        # This code checks for KeyError and redisplays the question form with an error message if choice isn't given.
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # After incrementing the choice count, the code returns an HttpResponseRedirect rather than a normal HttpResponse. 
        # HttpResponseRedirect takes a single argument: the URL to which the user will be redirected 
        # (see the following point for how we construct the URL in this case).
        #
        # As the Python comment above points out, you should always return an HttpResponseRedirect 
        # after successfully dealing with POST data. 
        # This tip isn't specific to Django; it's just good Web development practice.
        #
        # We are using the reverse() function in the HttpResponseRedirect constructor in this example. 
        # This function helps avoid having to hardcode a URL in the view function. 
        # It is given the name of the view that we want to pass control to 
        # and the variable portion of the URL pattern that points to that view. 
        # In this case, using the URLconf we set up in urls.py, 
        # this reverse() call will return a string like '/polls/3/results/'
        # where the 3 is the value of p.id. 
        # This redirected URL will then call the 'results' view to display the final page.
        #
        # Always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))