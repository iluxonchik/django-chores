from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import ChoreList, Chore

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
    
def newlist(request):
    if 'name' in request.POST and 'duedate' in request.POST:
        list = ChoreList(name=request.POST['name'], due_date=request.POST['duedate'])
        list.save()
        return HttpResponseRedirect('/chores/')
    return render(request, 'chores/newlist.html', {})

def detail(request, chorelist_id):
    # note the named pattern from urls.py, it has the same name as the 2nd parameter of this function,
    # which is how the id in the url will be mapped to chorelist_id parameter of this function
    # (?P<chorelist_id>[0-9]+)
    if 'name' in request.POST and 'duedate' in request.POST:
        iscomplete = 'iscomplete' in request.POST
        chore = Chore(chore_list=ChoreList.objects.get(pk=chorelist_id),name=request.POST['name'], due_date=request.POST['duedate'], complete=iscomplete)
        chore.save()
        
    lst = get_object_or_404(ChoreList, pk=chorelist_id)
    return render(request, 'chores/detail.html', {'chorelist':lst})
    """
    try:
        lst = ChoreList.objects.get(pk=chorelist_id)
    except ChoreList.DoesNotExist:
        raise Http404('Chore list with id {0} does not exist'.format(chorelist_id)) # message only shown in Debug mode
    return render(request, 'chores/detail.html', {'chorelist' : lst})
    """
        
def choredetail(request, chorelist_id, chore_id):
    list = get_object_or_404(ChoreList, pk=chorelist_id)
    chore = get_object_or_404(Chore, pk=chore_id)
    return render(request, 'chores/choredetail.html', {'chorelist':list, 'chore':chore})
    
def updatechore(request, chorelist_id, chore_id):
    chore = get_object_or_404(Chore, pk=chore_id)
    
    if 'complete' in request.POST:
        chore.complete = True
    else:
        chore.complete = False
    
    chore.save()
    return HttpResponseRedirect('/chores/' + chorelist_id + '/chores/' + chore_id)
    