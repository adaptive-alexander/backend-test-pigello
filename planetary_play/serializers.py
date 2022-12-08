from rest_framework import serializers
from .models import Planet, PlanetaryBody


# Serializers define the API representation.
class PlanetaryBodySerializer(serializers.HyperlinkedModelSerializer):
    orbits = serializers.HyperlinkedRelatedField(
        many=False,
        view_name='planetarybody-detail',
        read_only=True,
    lookup_field='name')

    class Meta:
        model = PlanetaryBody
        fields = ['url', 'name', 'gravity_constant', 'mass', 'volume', 'orbits']


class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planet
        fields = ['url', 'name', 'mass', 'gravity_constant', 'volume']
