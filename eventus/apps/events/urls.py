from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'apps.events.views.index', name="index"),
    
    url(r'^panel/$', 'apps.events.views.main_panel', name="panel"),
   
)
