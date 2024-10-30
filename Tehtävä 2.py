import requests

def hae_sää(paikkakunta, api_key):
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}"


    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        sääkuvaus = data["weather"][0]["description"]
        lämpötila = data["main"]["temp"]
        celsius = lämpötila - 273.15

    print(f"{paikkakunta}: {sääkuvaus.capitalize()}, Lämpötila: {celsius:.2f} °C")



if __name__ == "__main__":
    paikkakunta = input("Paikkakunta: ")
    api_key = "3d0cd6362a9e6cd1764c893bda35ff73"
    hae_sää(paikkakunta, api_key)