"""_summary_
"""
import requests
class FlightData():
    #This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        
        self.sheety_api_endpoint = "https://api.sheety.co/d227ad5bce98690ad95c1e66af319197/flightDeals/prices"
        self.desired_cities_flight_data = []
        self.iata_codes_flight_data = {}
        self.json_data_flight_data = {}
        self.prices = []
    def get_sheety_cities(self) -> list:
        self.json_data_flight_data = requests.get(url=self.sheety_api_endpoint,timeout=10).json()
        self.desired_cities_flight_data = [item['city'] for item in self.json_data_flight_data['prices'] if item['city']is not None]
        return self.desired_cities_flight_data
    
    def get_sheety_iata_pair(self) -> dict:
        self.iata_codes_flight_data = {item['city']:item['iataCode'] for item in self.json_data_flight_data['prices'] if item['city']is not None}
        return self.iata_codes_flight_data
    
    def modify_sheety_city_iata(self) -> dict:
        for item in self.json_data_flight_data['prices']:
            for key, value in self.iata_codes_flight_data.items():
                if item['city'] == key:
                    item['iataCode'] = value
        return self.iata_codes_flight_data
    
    def get_sheety_city_price(self) -> list:
        self.prices = [(item['city'],item['lowestPrice']) for item in self.json_data_flight_data['prices'] if item['city']is not None]
        return self.prices