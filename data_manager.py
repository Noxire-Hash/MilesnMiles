from pprint import pprint
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = os.getenv("SHEETY_ENDPOINT")
        self.data = {}

    def get_data(self):
        response = requests.get(url=f"{self.endpoint}")
        data = response.json()
        self.airport_data = data["prices"]
        return self.airport_data

    def update_iatacodes(self):
        for city in self.airport_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.endpoint}/{city['id']}", json=new_data)
            response.raise_for_status()
            pprint(response.text)

    def update_lowest_price(self, sheet_data):
        for city in sheet_data:
            new_data = {
                "price": {
                    "lowestPrice": city["lowestPrice"]
                }
            }
            response = requests.put(
                url=f"{self.endpoint}/{city['id']}", json=new_data)
            response.raise_for_status()
            pprint(response.text)
