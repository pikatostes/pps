# Ejemplo requests 02
import requests
import os

ciudad=input("Dime el nombre de una ciudad:")
# https://home.openweathermap.org/users/sign_up


api_key="12345678901234567890"
parametros={
        "q": ciudad,
        "mode":"json",
        "units":"metric",
        "APPID":api_key
}
r=requests.get("http://api.openweathermap.org/data/2.5/weather",params=parametros)

if r.status_code == 200:
    datos = r.json()
    print("La temperatura actual es:",datos["main"]["temp"])
else:
    print("De esa ciudad no tengo datos.")