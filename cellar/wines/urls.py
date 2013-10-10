from django.conf.urls import patterns, include, url

urlpatterns = patterns('cellar.wines.views',
        url(r'^wines/$', 'home', name='wines_home'),
)
