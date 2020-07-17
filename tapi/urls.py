from django.conf.urls import url 
from tapi import views
 
urlpatterns = [ 
    url(r'^api/tapi$', views.tapis_list),
    url(r'^api/tapi/(?P<pk>[0-9]+)$', views.tapis_detail),
    url(r'^api/patient$', views.papis_list),
    url(r'^api/patient/(?P<pk>[0-9]+)$', views.papis_detail),
    url(r'^api/item$', views.iapis_list),
    url(r'^api/item/(?P<pk>[0-9]+)$', views.iapis_detail),
    url(r'^api/salesmain$', views.smainapis_list),
    url(r'^api/salesmain/(?P<pk>[0-9]+)$', views.smainapis_detail),
    url(r'^api/salestran$', views.stranapis_list),
    url(r'^api/salestran/(?P<pk>[0-9]+)$', views.stranapis_detail)
]