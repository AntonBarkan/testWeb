from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	
    url(r'^login/', 'qa.views.log'),
    url(r'^signup/', 'qa.views.signup'),
    url(r'^question/(?P<id>[^/]+)/', 'qa.views.question'),
    url(r'^ask/', 'qa.views.ask'),
    url(r'^popular/', 'qa.views.popular'),
    url(r'^new/', 'qa.views.test'),
    url(r'^answer/', 'qa.views.answer'),
    url(r'^$', 'qa.views.all_q'),
)
