import requests

URL = "https://api.chucknorris.io/jokes/random"
response = requests.get(URL)

print(response.json()['value'])