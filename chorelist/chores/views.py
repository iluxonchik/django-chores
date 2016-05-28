from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# In Django, a View is just a function that returns an HTTP response

def index(request):
    # request represents an HTTP request that comes in
    return HttpResponse("Hello from the chores app")