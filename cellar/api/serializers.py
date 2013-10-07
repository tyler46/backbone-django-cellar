from rest_framework import serializers

from ..wines.models import Wine


class WineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wine
        fields = ('name', 'grapes', 'country', 'region',
                  'year', 'notes', 'picture') 
