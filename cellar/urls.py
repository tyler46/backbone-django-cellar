from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.static import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^cellar/', include('cellar.wines.urls')),
    # url(r'^$', 'cellar.views.home', name='home'),
    # url(r'^cellar/', include('cellar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('cellar.api.urls')),
)


urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += patterns('django.views',
            url(r'%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
                'static.serve', {'document_root': settings.MEDIA_ROOT,}),
    )
