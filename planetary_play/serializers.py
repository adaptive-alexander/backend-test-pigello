from rest_framework import serializers
from .models import Planet, PlanetaryBody


# Serializers define the API representation.
class PlanetaryBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetaryBody
        fields = ['id', 'name', 'gravity_constant', 'mass', 'volume', 'orbits']


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ['name', 'mass', 'gravity_constant', 'volume']
