from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# In Django, a View is just a function that returns an HTTP response

def index(request):
    # request represents an HTTP request that comes in
    return HttpResponse("You're at the ChoreList index")
    
def detail(request, chorelist_id):
    # note the named pattern from urls.py, it has the same name as the 2nd parameter of this function,
    # which is how the id in the url will be mapped to chorelist_id parameter of this function
    # (?P<chorelist_id>[0-9]+)
    return HttpResponse("You're looking at ChoreList #{0}".format(chorelist_id))
    
def chores(request, chorelist_id):
    return HttpResponse("You're looking at the Chores from ChoreList #{0}".format(chorelist_id))
    
def choredetail(request, chorelist_id, chore_id):
    return HttpResponse("You're looking at the Chore #{0} from ChoreList #{1}".format(chore_id, chorelist_id))