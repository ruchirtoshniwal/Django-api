from django.conf.urls import url 
from tapi import views
 
urlpatterns = [ 
    url(r'^api/tapi$', views.tapis_list),
    url(r'^api/tapi/(?P<pk>[0-9]+)$', views.tapis_detail)
]