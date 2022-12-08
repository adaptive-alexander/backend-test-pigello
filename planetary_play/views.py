from rest_framework import viewsets, response
from .models import Planet, PlanetaryBody
from planetary_play.serializers import PlanetSerializer, PlanetaryBodySerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


class PlanetaryBodyViewSet(viewsets.ViewSet):
    """
    API endpoint that allows planetary bodies to be viewed or edited.
    """
    queryset = PlanetaryBody.objects.all()
    serializer_class = PlanetaryBodySerializer

    def list(self, request):
        serializer = PlanetaryBodySerializer(self.queryset, many=True, context={'request': request})
        return response.Response(serializer.data)

    # @action(detail=False, methods=['post'], name="Add Planetary Body")
    # @csrf_exempt
    # def add_body(self, request):
    #     # Get data from request
    #     body_data = request.data
    #
    #     # Build planet
    #     planet = Planet.objects.get(pk=body_data.get("orbits"))
    #     planet_serial = PlanetSerializer(planet, context={'request': request})
    #     print(planet)
    #     print(planet_serial.data['url'])
    #
    #     # Add planet relation to body
    #     serializer = PlanetaryBodySerializer(data=body_data)
    #     serializer.orbits = planet_serial.data['url']
    #     # print(serializer.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(status=status.HTTP_201_CREATED)
    #     return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanetViewSet(viewsets.ViewSet):
    queryset = Planet.objects.all()

    def list(self, request):
        serializer = PlanetSerializer(self.queryset, many=True, context={'request': request})
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = PlanetSerializer(item, context={'request': request})
        return response.Response(serializer.data)
