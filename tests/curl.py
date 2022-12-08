import sqlite3
import requests
import json
from typing import List
from datetime import datetime as dt

url = "http://localhost:8000"


def list_planets():
    print(70 * '-')
    req = requests.get(url + "/planets/")
    print("List planets")
    print(f"Get request to /planets/:\n {json.dumps(req.json(), indent=4)}")
    print(70 * '-')


def list_orbiting_bodies(planet: str):
    print(70 * '-')
    req = requests.get(url + f"/planets/{planet}/bodies_orbit")
    print("List orbiting bodies planet")
    print(f"Get request to /planets/{planet}/bodies_orbit:\n {json.dumps(req.json(), indent=4)}")
    print(70 * '-')


def retrieve_planet(planet: str):
    print(70 * '-')
    req = requests.get(url + f"/planets/{planet}/")
    print("Information about a given planet")
    print(f"Get request to /planets/{planet}/:\n {json.dumps(req.json(), indent=4)}")
    print(70 * '-')


def list_planetary_bodies():
    print(70 * '-')
    req = requests.get(url + "/planetary_body/")
    print("List planetary bodies")
    print(f"Get request to /planetary_body/:\n {json.dumps(req.json(), indent=4)}")
    print(70 * '-')


def add_planetary_body(data: dict):
    print(70 * '-')
    req = requests.post(url + "/planetary_body/add_body/", json=data)
    print("Adding body")
    print(f"Post request to /planetary_body/addbody/:\n {json.dumps(req.json(), indent=4)}")
    print(70 * '-')


def update_body(body_id: int, data: dict):
    print(70 * '-')
    req = requests.patch(url + f"/planetary_body/{body_id}/", json=data)
    print("Updating orbiting body")
    print(f"Patch request to /planetary_body/{body_id}/:\n {json.dumps(req.json(), indent=4)}")
    print(70 * '-')


def delete_body(body_id: int):
    print(70 * '-')
    requests.delete(url + f"/planetary_body/{body_id}/")
    print("Remove orbiting body")
    print(f"Entry deleted")
    print(70 * '-')


def get_bulk_info(planets: List[str]):
    print(70 * '-')
    req = requests.post(url + "/planets/bulk_list_orbiting/", json=planets)
    print("Requesting list of orbiting bodies around planet")
    print(f"Post request to /planets/list_orbiting/:\n {json.dumps(req.json(), indent=4)}")
    print(70 * '-')


def get_sqlite_id() -> int:
    conn = sqlite3.connect("../db.sqlite3")
    cur = conn.cursor()
    cur.execute(
        f'SELECT id '
        f'FROM planetary_play_planetarybody '
        f'ORDER BY id DESC '
        f'LIMIT 1'
    )
    rows = cur.fetchall()
    return rows[0][0]


example_data = {
    "name": f'test {dt.utcnow()}',
    "mass": 1259125,
    "gravity_constant": 12.1,
    "volume": 124812,
    "orbits": "earth"
}

last_id = get_sqlite_id()

list_planets()

list_orbiting_bodies("earth")

retrieve_planet("earth")

list_planetary_bodies()

add_planetary_body(example_data)

update_body(last_id, example_data)

delete_body(last_id)

get_bulk_info(["earth", "mercury"])
