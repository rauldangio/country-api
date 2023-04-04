import requests


URL = "https://api.countrylayer.com/v2/all"
resposta = requests.get(URL)
print(resposta.content)