import requests
from config import FLIGHT_API_KEY

def get_flight_price(origin, destination, date):
    url = "https://api.tequila.kiwi.com/v2/search"
    headers = {"apikey": FLIGHT_API_KEY}
    params = {
        "fly_from": origin,
        "fly_to": destination,
        "date_from": date,
        "date_to": date,
        "curr": "USD",
        "limit": 1,
        "sort": "price"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if "data" in data and len(data["data"]) > 0:
        return data["data"][0]["price"]
    return None
