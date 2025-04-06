"""
Fortune Meya

This class interacts with the API
Returns info about the weather if the API status code is 200(Successful)
Returns an error if the API status code is anything other than 200
"""

import requests


class WeatherApi:
    def __init__(self,api_key):
        self.api_key=api_key
        self.weather_url = "https://api.openweathermap.org/data/2.5/forecast"


    def get_weather(self,city_info):
        url = f'{self.weather_url}?q={city_info}&appid={self.api_key}&units=imperial'
        response = requests.get(url)
        if response==200:
            return response.json()
        else:
            none= f'Could not find the weather for {city_info}'
            return none
