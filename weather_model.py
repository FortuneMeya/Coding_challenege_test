"""
Fortune Meya

This class organizes the necessary information needed from the API
Returns the saved information from the database
"""
class WeatherModel:
    def __init__(self,city,temperature,desc,time,weather_respo):
        self.city = city
        self.temperature = temperature
        self.desc = desc
        self.time = time
        self.weather_respo= weather_respo
    def transfer_info(self):
       return self.weather_respo.save(self)
