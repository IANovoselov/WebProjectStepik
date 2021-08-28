from django.urls import include, path
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
   path(r'^$', 'qa.views.test'),
   path(r'^login/.*$', 'qa.views.test', name='login'),
   path(r'^signup/.*', 'qa.views.test', name='signup'),
   path(r'^question/(?P<id>[0-9]+)/$', 'qa.views.test', name='question'),
   path(r'^ask/.*', 'qa.views.test', name='ask'),
   path(r'^popular/.*', 'qa.views.test', name='popular'),
   path(r'^new/.*', 'qa.views.test', name='new'),
]