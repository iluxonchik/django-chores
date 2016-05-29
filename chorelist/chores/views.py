from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import ChoreList

# Create your views here.
# In Django, a View is just a function that returns an HTTP response

def index(request):
    # request represents an HTTP request that comes in
    lists = ChoreList.objects.all()
    context = {'chorelists' : lists,}
    return render(request, 'chores/index.html', context) # equivalent to comment below
    """
    template = loader.get_template('chores/index.html')
    context = RequestContext(request, {
       'chorelists' : lists,
    })
    return HttpResponse(template.render(context)) # render template with the specified context
    """
    
def detail(request, chorelist_id):
    # note the named pattern from urls.py, it has the same name as the 2nd parameter of this function,
    # which is how the id in the url will be mapped to chorelist_id parameter of this function
    # (?P<chorelist_id>[0-9]+)
    lst = get_object_or_404(ChoreList, pk=chorelist_id)
    return render(request, 'chores/detail.html', {'chorelist':lst})
    """
    try:
        lst = ChoreList.objects.get(pk=chorelist_id)
    except ChoreList.DoesNotExist:
        raise Http404('Chore list with id {0} does not exist'.format(chorelist_id)) # message only shown in Debug mode
    return render(request, 'chores/detail.html', {'chorelist' : lst})
    """
    
def chores(request, chorelist_id):
    return HttpResponse("You're looking at the Chores from ChoreList #{0}".format(chorelist_id))
    
def choredetail(request, chorelist_id, chore_id):
    return HttpResponse("You're looking at the Chore #{0} from ChoreList #{1}".format(chore_id, chorelist_id))