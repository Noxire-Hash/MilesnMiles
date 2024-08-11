class FlightData:
    def __init__(self, flight_search_instance):
        self.fs = flight_search_instance

    def parse_data(self, flight_data_raw, sort=False):
        parsed_data = []
        try:
            for offer in flight_data_raw['data']:
                flight_info = {
                    'price': offer['price']['grandTotal'],
                    'currency': offer['price']['currency'],
                    'departure': offer['itineraries'][0]['segments'][0]['departure']['iataCode'],
                    'arrival': offer['itineraries'][0]['segments'][0]['arrival']['iataCode'],
                    'departure_time': offer['itineraries'][0]['segments'][0]['departure']['at'].replace('T', ' '),
                    'arrival_time': offer['itineraries'][0]['segments'][0]['arrival']['at'].replace('T', ' '),
                    'airline': offer['validatingAirlineCodes'][0],
                }

                # Check if return segment exists
                if len(offer['itineraries']) > 1:
                    flight_info['return_departure_time'] = offer['itineraries'][1]['segments'][0]['departure']['at'].replace(
                        'T', ' ')
                    flight_info['return_arrival_time'] = offer['itineraries'][1]['segments'][0]['arrival']['at'].replace(
                        'T', ' ')
                else:
                    flight_info['return_departure_time'] = None
                    flight_info['return_arrival_time'] = None

                parsed_data.append(flight_info)
        except KeyError as e:
            print(f"Unexpected data format: {e}")

        if sort:
            sorted_data = self.sort_data(parsed_data)
            return sorted_data
        else:
            return parsed_data

    def sort_data(self, flight_data):
        return sorted(flight_data, key=lambda x: x['price'])

    def format_data(self, flight_data):
        formatted_data = []
        for flight in flight_data:
            departure_airport = self.fs.reverse_airport_code(
                flight['departure']) or "Unknown"
            arrival_airport = self.fs.reverse_airport_code(
                flight['arrival']) or "Unknown"
            airline = self.fs.reverse_airline_code(
                flight['airline']) or "Unknown"

            formatted_data.append(
                f"Price: {flight['price']} {flight['currency']}\n"
                f"From: {departure_airport} to {arrival_airport}\n"
                f"Departure: {flight['departure_time']}\n"
                f"Arrival: {flight['arrival_time']}\n"
                f"Return Departure: {flight['return_departure_time']}\n"
                f"Return Arrival: {flight['return_arrival_time']}\n"
                f"Airline: {airline}\n"
                "----------------------------------------"
            )
        return formatted_data
