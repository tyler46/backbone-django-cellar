from django.conf.urls import *

from tastypie.api import Api

from .resources import WineResource


v1_api = Api(api_name='v1')

v1_api.register(WineResource())

wine_resource = WineResource()


urlpatterns = patterns('cellar.api.urls',
    # The normal jazz here ...
    (r'^', include(v1_api.urls)),
)
