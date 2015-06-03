# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cdrport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pabx/$', views.pabx, name='pabx'),
    url(r'^ramal/$', views.editar_ramal, name='editar_ramal'),
    #url(r'^gerar-call/$', views.gerar_call, name='gerar_call'),
    #url(r'^gerar-call/(?P<origem>\d+)/$', views.gerar_call, name='gerar_call'),
    #url(r'^gerar-call/(?P<origem>\d+)/(?P<destino>\d+)/$', views.gerar_call, name='gerar_call'),
    url(r'^ramal-alterado/$', views.editar_ramal_ok, name='ramal_ok'),
    url(r'^ramal/(?P<name>\d+)/$', views.editar_ramal, name='editar_ramal'),

)
