from django.conf.urls import url 
from tapi import views
 
urlpatterns = [ 
    url(r'^api/type$', views.tapis_list),
    url(r'^api/type/(?P<pk>[0-9]+)$', views.tapis_detail),
    url(r'^api/patient$', views.papis_list),
    url(r'^api/patient/(?P<pk>[0-9]+)$', views.papis_detail),
    url(r'^api/item$', views.iapis_list),
    url(r'^api/item/(?P<pk>[0-9]+)$', views.iapis_detail),
    url(r'^api/salesmain$', views.smainapis_list),
    url(r'^api/salesmain/(?P<pk>[^/]+)$', views.smainapis_detail),
    url(r'^api/salestran$', views.stranapis_list),
    url(r'^api/salestran/(?P<pk>[^/]+)$', views.stranapis_detail),
    url(r'^api/ledger$', views.ledgerapis_list),
    url(r'^api/ledger/(?P<pk>[^/]+)$', views.ledgerapis_detail),
    url(r'^api/bookmaster$', views.bookmasterapis_list),
    url(r'^api/bookmaster/(?P<pk>[0-9]+)$', views.bookmasterapis_detail)
]