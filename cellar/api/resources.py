from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from .utils import PrettyJSONSerializer

from ..wines.models import Wine

class WineResource(ModelResource):
    """Model Resource for exposing wine objects through API."""

    class Meta:
        queryset = Wine.objects.all()
        resource_name = 'wines'
        authentication = Authentication()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'delete']
        serializer = PrettyJSONSerializer(formats=['json'])
