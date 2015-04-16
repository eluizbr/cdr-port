from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cdrport.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^time/$', views.time_line, name='time_line'),
)
