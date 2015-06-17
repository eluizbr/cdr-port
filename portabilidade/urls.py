# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cdrport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<numero>\d+)$', views.consulta, name='consulta'),

)
