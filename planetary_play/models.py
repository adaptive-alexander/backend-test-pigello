from django.db import models


# Represents a planet in the system
class Planet(models.Model):
    name = models.CharField(max_length=50)
    mass = models.FloatField()
    gravity_constant = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return self.name


# Represents a celestial body orbiting a planet
class PlanetaryBody(models.Model):
    name = models.CharField(max_length=50)
    mass = models.FloatField()
    gravity_constant = models.FloatField()
    volume = models.FloatField()
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
