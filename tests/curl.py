import requests
import json
from datetime import datetime as dt

url = "http://localhost:8000"

req = requests.get(url + "/planets/")
print(f"Get request to /planets/:\n {req.json()}")

req = requests.get(url + "/planets/earth/")
print(f"Get request to /planets/earth/:\n {req.json()}")

req = requests.get(url + "/planetary_body/")
print(f"Get request to /planetary_body/:\n {req.json()}")

# req = requests.post(url + "/planetary_body/add_body/", data=json.dumps({
#     "name": f'test {dt.utcnow()}',
#     "mass": 1259125,
#     "gravity_constant": 12.1,
#     "volume": 124812,
#     "orbits": "earth"
# }))
#
# print(f'Post status: {req.status_code}')
# print(f"Post request to /planetary_body/:\n {req.json()}")
