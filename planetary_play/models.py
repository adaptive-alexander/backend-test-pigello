from django.db import models


# Represents a planet in the system
class Planet(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    mass = models.FloatField()
    gravity_constant = models.FloatField()
    volume = models.FloatField()
    # There could be use adding a bodyType here

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# Represents a planetary body orbiting a planet
class PlanetaryBody(models.Model):
    name = models.CharField(max_length=50)
    mass = models.FloatField()
    gravity_constant = models.FloatField()
    volume = models.FloatField()
    orbits = models.ForeignKey(Planet, on_delete=models.CASCADE)
    # There could be use adding a bodyType here

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
