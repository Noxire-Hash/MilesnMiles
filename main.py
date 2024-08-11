import data_manager
import flight_search
import notification_manager
import flight_data
from pprint import pprint


# dataManager = data_manager.DataManager()
# flightSearch = flight_search.FlightSearch()
# flightData = flight_data.FlightData(flightSearch)
# sheet_data = dataManager.get_data()
commands = """
Available commands:
- Search: Search for the lowest price for all cities in the sheet.
- Search from, to, stay, currency: Search for the lowest price for a specific city in the sheet.
  Example: Search Istanbul London 3 GBP
  Default values are: from: IST, to: LON, stay: 3, currency: GBP
  You can use IATA codes for cities as well.
- Send Email: Send an email to the user with the lowest price for selected cities in the sheet.
- Exit: Exit the program.
- get_iata_code --FORCE: Get IATA codes for all cities in the sheet if the program couldn't auto find it.
"""


cli_open = True
while cli_open:
    input("Welcome to Miles&Miles ! ")
    for command in commands.split("\n"):
        print(command)


# if sheet_data[0]["iataCode"] == "":
#     for row in sheet_data:
#         row["iataCode"] = flightSearch.get_iata_code(row["city"])
#     dataManager.airport_data = sheet_data
#     dataManager.update_iatacodes()
# elif sheet_data[0]["iataCode"] != "":
#     print("sheet data already has iataCode, if there is a mistake you can use $ get_iata_code --FORCE for updating iataCode")

# flight_data_raw = flightSearch.get_flight_data()
# formatted_data = flightData.parse_data(flight_data_raw, sort=True)
# pprint(formatted_data)
# flight_data_raw = flightSearch.get_flight_data()
# parsed_data = flightData.parse_data(flight_data_raw, sort=True)
# formatted_data = flightData.format_data(parsed_data)

# for data in formatted_data:
#     print(data)

# if parsed_data:
#     lowest_price = parsed_data[0]["price"]
#     print(f"Lowest price: {lowest_price}")

#     for row in sheet_data:
#         row["lowestPrice"] = lowest_price
#         dataManager.update_lowest_price(sheet_data)
# else:
#     print("No flight data available.")

# lowest_price = formatted_data[0]["price"]
# print(f"Lowest price: {lowest_price}")
# for city in sheet_data:
#     flight_data_raw = flightSearch.get_flight_data(
#         origin_city="IST", destination_city=city["iataCode"])
#     parsed_data = flightData.parse_data(flight_data_raw, sort=True)
#     formatted_data = flightData.format_data(parsed_data)
#     if parsed_data:
#         lowest_price = parsed_data[0]["price"]
#         print(f"Lowest price: {lowest_price}")

#         for row in sheet_data:
#             row["lowestPrice"] = lowest_price
#             dataManager.update_lowest_price(sheet_data)
