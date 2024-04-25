from flight_data import FlightData
from flight_search import FlightSearch
import asyncio
import datetime

class DataManager(FlightData,FlightSearch):
    """This class is responsible for managing both classes.
    It calls and manages the methods from both classes.
    """
    

    def __init__(self):
        FlightData.__init__(self)
        FlightSearch.__init__(self)
        self.desired_cities = []
        self.iata_codes = {}
        self.json_data = {}
        self.args = {}
        self.my_desired_city_price = {}
        self.available_flights = []
        self.fly_to = ""
  


    def get_destination_cities(self):
        
        self.desired_cities = super().get_sheety_cities()
        return self.desired_cities
    
    def get_iata_codes(self) -> dict:
        self.iata_codes = self.get_sheety_iata_pair()
        return self.iata_codes
    
    def get_city_iata_info(self):
        self.iata_codes= super().get_iata_code_tequila(self.iata_codes)
        return self.iata_codes
    
    def decide_if_city_in_sheety(self):
        fly_from_city =str(input("Enter the city you are flying from: ")).title()
        if fly_from_city in self.desired_cities:
            self.fly_from = self.iata_codes[fly_from_city]
        else:
            self.fly_from = self.get_iata_code_tequila(fly_from_city)

    def convert_date_for_tequila_call(self):
        strings_to_replace = ["|", "-", " ", "_",'.',',','\\']
        self.date_from = str(input("Enter the date you want to fly from: "))
        for string in strings_to_replace:
            self.date_from = self.date_from.replace(string,"/")
        self.date_to = str(input("Enter the date you want to fly to: "))
        for string in strings_to_replace:
            self.date_to = self.date_to.replace(string,"/")

    async def bring_data_for_iata(self):
        self.decide_if_city_in_sheety()
        self.convert_date_for_tequila_call()
        for value in self.iata_codes.values():
            self.fly_to = value
            self.tequila_call_args = {
                "fly_from": self.fly_from,
                "fly_to": self.fly_to,
                "date_from": self.date_from,
                "date_to": self.date_to,
                "curr": "EUR",
                "max_stopovers": 0
            }
            
            await self.destination_search_tequila(self.tequila_call_args)  # Fix: Pass the arguments as keyword arguments
            self.available_flights.extend(self.create_flights_dict_tequila())   # Fix: Await the result of create_flights_dict_tequila()
            
    async def check_lowest_price(self):
        self.my_desired_city_price = super().get_sheety_city_price()
        for city, price in self.my_desired_city_price:
            for flight in self.available_flights:
                if flight['cityTo'] == city and flight['price'] < price:
                    departure_time_str = flight['local_departure']
                    departure_date_time = datetime.datetime.strptime(departure_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                    departure_date = departure_date_time.strftime("%d-%m-%Y")
                    departure_time = departure_date_time.strftime("%H:%M")
                    # -------------------------- #
                    arrival_time_str = flight['local_arrival']
                    arrival_date_time = datetime.datetime.strptime(arrival_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                    arrival_date = arrival_date_time.strftime("%d-%m-%Y")
                    arrival_time = arrival_date_time.strftime("%H:%M")
                    print(f"Low price alert! Only €{flight['price']} to fly from {flight['cityFrom']} - {flight['cityTo']}, from {departure_date} | {departure_time} to {arrival_date} | {arrival_time}.")
                        




async def main():
    data_manager = DataManager()
    data_manager.get_destination_cities()
    data_manager.get_iata_codes()
    data_manager.get_city_iata_info()
    
    await data_manager.bring_data_for_iata()
    print(data_manager.available_flights)
    await data_manager.check_lowest_price()
    

if __name__ == "__main__":
    asyncio.run(main())
