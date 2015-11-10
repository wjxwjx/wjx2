from django.conf.urls import patterns, include, url
from django.contrib import admin
from books.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', window),
    url(r'gosearch/$', gosearch),
    url(r'search/$', search),
    
    url(r'showlist/$', showlist),
    url(r'detail/(.+)$', detail),
    url(r'delete/(.+)$', delete),
    url(r'redo/(.+)$', redo),
    url(r'addbook/$', addbook),
    url(r'added/$', added),
    url(r'toaddauthored/$',toaddauthored ),
    url(r'redone/$',redone),
     url(r'^admin/', include(admin.site.urls)),
)
