from rest_framework import viewsets

from .serializers import WineSerializer

from ..wines.models import Wine


class WineViewSet(viewsets.ModelViewSet):
    """API endpoint that allows wines to be viewed or edited."""
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
