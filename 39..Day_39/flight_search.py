"""
This file is responsible for talking to the Flight Search API and returning flights.
"""
import os
import requests
import httpx 

class FlightSearch():
    """
    This class is responsible for talking to the Flight Search API.
    """
    def __init__(self) -> None:
        self.url_tequilla = "https://tequila-api.kiwi.com/"
        self.locations_endpoint = "locations/query"
        self.api_key = os.environ["TEQUILLA_API_KEY"]
        self.search_location_endpoint = 'v2/search'
        self.data = {}
        self.destination_data = {}
    def get_flight_info_tequila(self,location: str) -> dict:
        """_summary_
        This method is responsible for talking to the Flight Search API.
        """
        headers = {
            "apikey": self.api_key
        }
        parameters = {
            "term": location
        }
        response = requests.get(url=f"{self.url_tequilla}{self.locations_endpoint}",
                            headers=headers, params=parameters, timeout=10)
        response.raise_for_status()
        self.data = response.json()
        
        return self.data
    
    def get_iata_code_tequila(self,location):
        """_summary_
        This method is responsible for getting the IATA code from the Flight Search API.
        """
        if  isinstance(location,dict) and location is not None:
            for key,value in location.items():
                self.get_flight_info_tequila(key)
                if self.data['locations'][0]['name'] =='Tokyo':
                    val = self.data['locations'][3]['code']
                else:
                    val = self.data['locations'][0]['code']
                location[key] =  val # REMEBER HERE WAS CHANGED AND ABOVE
        else:
            self.get_flight_info_tequila(location)
            if self.data['locations'][0]['name'] =='Tokyo':
                location = self.data['locations'][3]['code']
            else:
                location = self.data['locations'][0]['code']
        return location

    async def destination_search_tequila(self,parameters:dict) -> dict:
        """_summary_
        This method is responsible for searching for the destination.
        eg: Args:
            {"fly_from": "Iata Code (UPPER)",
                "fly_to": 'Iata Code (UPPER)',
                "date_from": "01/01/2022",
                "date_to": "01/01/2023",
                "curr": "EUR",
                "max_stopovers": 0}
        """
        headers = {
            "apikey": self.api_key
        }
        params = parameters
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url=f"{self.url_tequilla}{self.search_location_endpoint}",
                                        headers=headers, params=params, timeout=10)
                response.raise_for_status()  # Will raise an exception for 4XX/5XX responses
                self.destination_data = response.json()
            except httpx.HTTPStatusError as e:
               print(f"An error occurred: {e.response.status_code} : {e.response.text}")
        return self.destination_data

    def create_flights_dict_tequila(self) -> dict|list:
        keys_of_interest =[ 'flyFrom','flyTo','cityFrom','cityTo', 'local_departure', 'local_arrival', 'utc_departure', 'utc_arrival','price']
        list_of_dicts_of_interest = [{key: val[key] for key in keys_of_interest} for val in self.destination_data['data']]
        return list_of_dicts_of_interest

    



    
        