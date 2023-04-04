import json

import requests

URL = "https://restcountries.com/v3.1/all"
URL_NAME = "https://restcountries.com/v3.1/name/brazil"
resposta = requests.get(URL_NAME)

paises = json.loads(resposta.text)

for pais in paises:
    print(pais['capital'])