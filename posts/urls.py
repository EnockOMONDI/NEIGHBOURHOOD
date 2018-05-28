from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.BusinessList.as_view(), name='all'),
    url(r'new/$', views.CreateBusiness.as_view(), name='create'),
    url(r'by/(?P<username>[-\w]+)', views.UserBusinesses.as_view(), name='for_user'),
    url(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.BusinessDetail, name='single'),
    url(r'delete/(?P<pk>\d+)/$', views.DeleteBusiness.as_view(), name='delete')
]
