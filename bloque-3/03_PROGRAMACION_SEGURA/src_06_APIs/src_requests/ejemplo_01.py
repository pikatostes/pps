# Ejemplo request 01
import requests

URL = "https://swapi.dev/api/people/1"

r = requests.get(URL)

print(r.status_code)
datos=r.json()
print(datos["name"])

# (venv) alu@xdebian11:$ curl https://swapi.dev/api/people/1 | json_pp
