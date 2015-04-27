# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cdrport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^consulta/$', views.cdr_serach, name='consulta'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^error/$', views.error, name='error'),
)
