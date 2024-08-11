import requests
from dotenv import load_dotenv
import os
import datetime
from pprint import pprint


class FlightSearch:
    def __init__(self):
        load_dotenv()
        self.endpoint = os.getenv("AMADEUS_ENDPOINT")
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.api_secret = os.getenv("AMADEUS_API_SECRET")
        self.token = self.get_token()
        self.today = str(datetime.datetime.now()).split(" ")[0]

    def get_token(self):
        response = requests.post(
            url=f"{self.endpoint}/v1/security/oauth2/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "client_credentials",
                "client_id": self.api_key,
                "client_secret": self.api_secret
            }
        )
        response.raise_for_status()
        return response.json()["access_token"]

    def get_iata_code(self, city_name):
        params = {"keyword": city_name,
                  "max": 2,
                  "include": "AIRPORTS"}
        response = requests.get(
            headers={"Authorization": f"Bearer {self.token}"},
            url=f"{self.endpoint}/v1/reference-data/locations/cities",
            params=params
        )
        print(f"Status Code: {
              response.status_code}. Airport Iata Code: {response.text}")
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"No airport found for {city_name}.")
            return "Airport can't be found"
        except KeyError:
            print("No 'iataCode' key in response.")
            return "No iata code in response"
        return code

    def get_flight_data(self, origin_city="IST", destination_city="LON", currency="GBP", stay_days=3):
        params = {
            "originLocationCode": origin_city,
            "destinationLocationCode": destination_city,
            "departureDate": self.today,
            "returnDate": str(datetime.datetime.now() + datetime.timedelta(days=stay_days)).split(" ")[0],
            "adults": 1,
            "nonStop": "true",
            "currencyCode": currency,
            "max": 3
        }
        response = requests.get(
            headers={"Authorization": f"Bearer {self.token}"},
            url=f"{self.endpoint}/v2/shopping/flight-offers",
            params=params
        )
        if response.status_code != 200:
            print(f"Something went wrong. Status Code: {
                  response.status_code}. Response: {response.json()}")
            return None

        return response.json()

    def reverse_airport_code(self, code):
        params = {"subType": "AIRPORT", "keyword": code}
        response = requests.get(
            headers={"Authorization": f"Bearer {self.token}"},
            url=f"{self.endpoint}/v1/reference-data/locations",
            params=params
        )
        return response.json()["data"][0]["name"]

    def reverse_airline_code(self, code):
        params = {"airlineCodes": code}
        response = requests.get(
            headers={"Authorization": f"Bearer {self.token}"},
            url=f"{self.endpoint}/v1/reference-data/airlines",
            params=params
        )
        return response.json()["data"][0]["commonName"]
