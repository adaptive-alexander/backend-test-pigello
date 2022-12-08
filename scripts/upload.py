import requests
from planetary_play.models import Planet, PlanetaryBody

def run():
    planets = requests.get("https://api.le-systeme-solaire.net/rest/bodies").json()
    planets = [rec for rec in planets.get('bodies') if rec.get('bodyType') == "Planet"]

    for planet in planets:
        planet_obj = Planet(
            name=f'{planet.get("englishName").lower()}',
            mass=(planet.get("mass").get("massValue")) * 10 ** (planet.get("mass").get("massExponent")),
            gravity_constant=planet.get('gravity'),
            volume=planet.get('vol').get('volValue') * 10 ** planet.get('vol').get('volExponent')
        )
        planet_obj.save()
        print(f'Planet {planet.get("englishName")} uploaded')
        try:
            moons = planet.get('moons')
            moon_links = [moon.get('rel') for moon in moons]
            print("Moons:")
            print(moon_links)
        except:
            print(f'Planet {planet.get("englishName")} has no moons')
