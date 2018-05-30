from django.conf.urls import url
from . import views

app_name = 'neighbourhoodapp'

urlpatterns = [
    url(r'^$', views.ListNeighbourhoods.as_view(), name='all'),
    url(r'^new/$', views.CreateNeighbourhood.as_view(), name='create'),
    url(r'^businesses/in/$(?P<slug>[-\w]+)/$', views.SingleNeighbourhood.as_view(), name='single'),
    url(r'join/(?P<slug>[-\w]+)/$', views.JoinNeighbourhood.as_view(), name='join'),
    url(r'leave/(?P<slug>[-\w]+)/$', views.LeaveNeighbourhood.as_view(), name='leave'),
]
