from rest_framework import viewsets, response
from .models import Planet, PlanetaryBody
from planetary_play.serializers import PlanetSerializer, PlanetaryBodySerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status


class PlanetaryBodyViewSet(viewsets.ViewSet):
    """
    API endpoint that allows planetary bodies to be viewed or edited.
    """
    queryset = PlanetaryBody.objects.all()
    serializer_class = PlanetaryBodySerializer

    def list(self, request):
        """
        Lists all existing planetary bodies.
        """
        # Retrieve all objects in self.queryset.
        serializer = PlanetaryBodySerializer(self.queryset, many=True, context={'request': request})
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieves a single planetary body.
        """
        # Retrieve and serialize a single object from self.queryset based on pk.
        body = get_object_or_404(self.queryset, pk=pk)
        serializer = PlanetSerializer(body, context={'request': request})
        return response.Response(serializer.data)

    def destroy(self, request, pk=None):
        """
        Removes a planetary body by id.
        """
        # Retrieve a single object from self.queryset
        body = get_object_or_404(self.queryset, pk=pk)

        # Delete object
        body.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """
        Updates (partial accepted) a planetary body by id.
        """
        # Retrieve single object from self.queryset based on pk
        body = get_object_or_404(self.queryset, pk=pk)
        serializer = PlanetaryBodySerializer(body, data=request.data, partial=True)

        # Error handling
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], name="Add Planetary Body")
    def add_body(self, request):
        """
        Adds a new body to orbit a planet.
        """
        # Get data from request
        body_data = request.data

        # Build planet
        planet = Planet.objects.get(pk=body_data.get("orbits"))

        # Add planet relation to body
        serializer = PlanetaryBodySerializer(data=body_data)
        serializer.orbit = planet

        # Error handling
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanetViewSet(viewsets.ViewSet):
    """
    API endpoint to view information about planets.
    """
    queryset = Planet.objects.all()

    def list(self, request):
        """
        Lists all planets.
        """
        # Retrieve and serialize all objects in to self.queryset
        serializer = PlanetSerializer(self.queryset, many=True, context={'request': request})
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieves information about a given planet.
        """
        # Retrieve and serialize single object in self.queryset base on pk
        planet = get_object_or_404(self.queryset, pk=pk)
        serializer = PlanetSerializer(planet, context={'request': request})
        return response.Response(serializer.data)

    @action(detail=True, methods=["get"])
    def bodies_orbit(self, request, pk=None):
        """
        Get information about the planetary bodies orbiting a given planet.
        param:
        pk - str: name of planet.
        """
        # Get queryset from PlanetaryObjects based on filter where orbits_id=pk
        qs = PlanetaryBody.objects.filter(orbits_id=pk)

        # Serialize queryset in list comprehension
        ser = [PlanetaryBodySerializer(q).data for q in qs]

        return response.Response(ser, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], name="Add Planetary Body")
    def bulk_list_orbiting(self, request):
        """
        Lists planetary objects orbiting a list of planets.
        params:
        request - List[str]: A list of strings of planets to list data for.
        """
        # Get data from request
        planet_list = request.data

        # Serializer used to create a list of serialized data
        serializer = []

        for planet in planet_list:
            # Queryset of planetary bodies with orbits_id = planet
            # This could potentially be done more efficiently with reverse, have yet to benchmark
            qs = PlanetaryBody.objects.filter(orbits_id=planet)

            # Serialize PlanetaryBody queryset
            serializer += [PlanetaryBodySerializer(q).data for q in qs]

            # Get and serialize planet and add to serialize list
            planet_obj = Planet.objects.get(name=planet)
            serializer += [PlanetSerializer(planet_obj).data]

        for entry in serializer:
            # Try to compute density + error handling
            try:
                # Computation on the fly. This is ok for small amounts of data.
                # Should the data grow larger or requests higher volumes, consider pre-compute in database.
                # Not well suited for caching.
                entry['density'] = entry.get('mass') / entry.get('volume')

            # If data is 0
            except ZeroDivisionError:
                print(f'Could not compute density for {entry}, 0 values')

            # TypeError, most likely None (or null)
            except TypeError:
                print(f"Could not compute density for {'entry'}, invalid data")

        return response.Response(serializer, status=status.HTTP_200_OK)
