class WeatherService:
    def __init__(self, weather_respo, api_info):
        self.weather_respo= weather_respo
        self.api_info = api_info

    def get_weather_data(self, city: str):
        data = self.api_info.get_weather(city)
        self.weather_respo.save(data)



