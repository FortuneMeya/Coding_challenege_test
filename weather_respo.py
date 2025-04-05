class WeatherRespo:
    def __init__(self,database):
        self.database = database

    def save(self,weather_data):
        self.database.add(weather_data)
        self.database.commit()

    def get_city_weather(self,city :str):
        return self.database(city)