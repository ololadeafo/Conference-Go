import requests
from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def get_photo(city, state):
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    url = f"https://api.pexels.com/v1/search?query={city}+{state}"
    response = requests.get(url, headers=headers)
    print(response)
    return response.json()["photos"][0]["url"]


def get_weather_data(city, state):
    parameters = {
        "q": f"{city},{state},US",
        "appid": OPEN_WEATHER_API_KEY
    }
    url = "http://api.openweathermap.org/geo/1.0/direct"
    response = requests.get(url, parameters=parameters)
    content = response.json()
    try:
        lat = content[0]["lat"]
        lon = content[0]["lon"]
    except (KeyError, IndexError):
        return None
    parameters = {
        "lat": lat,
        "lon": lon,
        "units": "imperial",
        "appid": OPEN_WEATHER_API_KEY
    }
    url = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url, parameters=parameters)
    json_response = response.json()

    try:
        temp = json_response["main"]["temp"]
        description = json_response["weather"][0]["description"]
    except (KeyError, IndexError):
        return None

    return {"temp": temp, "description": description}
