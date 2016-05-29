from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<chorelist_id>[0-9]+)/$', views.detail, name='detail'), # NOTE: naming of named regex is important (see views.py for more)
    url(r'^(?P<chorelist_id>[0-9]+)/chores/$', views.chores, name='chores'),
    url(r'^(?P<chorelist_id>[0-9]+)/chores/(?P<chore_id>[0-9]+)/$', views.choredetail, name='choredetail'),
    
]