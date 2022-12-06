from rest_framework import viewsets
from .models import Planet, PlanetaryBody
from rest_framework import permissions
from planetary_play.serializers import PlanetSerializer, PlanetaryBodySerializer


class PlanetaryBodyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PlanetaryBody.objects.all()
    serializer_class = PlanetaryBodySerializer
    permission_classes = [permissions.IsAuthenticated]


class PlanetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlanetaryBodyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PlanetaryBody.objects.all()
    serializer_class = PlanetaryBodySerializer
    permission_classes = [permissions.IsAuthenticated]
