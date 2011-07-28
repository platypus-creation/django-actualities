from django.conf.urls.defaults import *


urlpatterns = patterns('',
   url(r'^$', 'actualities.views.list'),
   url(r'^(?P<year>[\d]{4})/(?P<month>[\d]{2})/(?P<day>[\d]{2})/(?P<slug>[\w\-]+)/$', 'actualities.views.actuality'),
)