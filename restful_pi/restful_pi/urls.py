from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restful_pi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^outputs/', include('outputs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
