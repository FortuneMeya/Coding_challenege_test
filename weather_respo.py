"""
Fortune Meya

This class is used to store the information into the database
Returns the information that was added into the database
"""

class WeatherRespo:
    def __init__(self,database):
        self.database = database

    def save(self,weather_model):
        self.database.add(weather_model)
        self.database.commit()

    def get_city_weather(self,city :str):
        return self.database(city)