from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),	
    url(r'^login/', 'qa.views.test'),
    url(r'^signup/', 'qa.views.test'),
    url(r'^question/(?P<id>[^/]+)/', 'qa.views.question'),
    url(r'^ask/', 'qa.views.test'),
    url(r'^popular/', 'qa.views.popular'),
    url(r'^new/', 'qa.views.test'),
    url(r'^$', 'qa.views.all_q'),
)
