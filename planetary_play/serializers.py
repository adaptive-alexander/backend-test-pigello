from rest_framework import serializers
from .models import Planet, PlanetaryBody


# Serializers define the API representation.
class PlanetaryBodySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanetaryBody
        fields = ['name', 'gravity_constant', 'mass', 'volume']


class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planet
        fields = ['name', 'gravity_constant', 'mass', 'volume']
