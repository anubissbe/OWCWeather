"""
OWCWeather - Simple Python app to fetch and display current weather data using OpenWeather API.

How to Use:
1. Install dependencies: pip install requests
2. Replace "your_openweather_api_key_here" with your actual API key.
3. Run the app and use `app.print_weather("City Name")` to get weather data.

Credits:
This project was created and maintained by [anubissbe](https://github.com/anubissbe).
Source code: https://github.com/anubissbe/OWCWeather
"""

import requests

class WeatherApp:
    def __init__(self):
        self.valves = Valves()

    def get_current_weather(self, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={self.valves.units}&lang={self.valves.language}&appid={self.valves.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return self._process_weather_data(data)
        else:
            return {"error": "Failed to retrieve weather data."}

    def _process_weather_data(self, data):
        weather = {
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "weather_description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }

        # Apply translations
        translations = {
            "temperature": "Temperature",
            "feels_like": "Feels Like",
            "weather_description": "Weather Description",
            "humidity": "Humidity",
            "wind_speed": "Wind Speed",
        }

        for key, value in translations.items():
            if key in weather:
                weather[key] = value

        # Format units
        if self.valves.units == "metric":
            weather["temperature"] = f"{weather['temperature']}°C"
            weather["feels_like"] = f"{weather['feels_like']}°C"
            weather["wind_speed"] = f"{weather['wind_speed']} m/s"
        else:
            weather["temperature"] = f"{weather['temperature']}°F"
            weather["feels_like"] = f"{weather['feels_like']}°F"
            weather["wind_speed"] = f"{weather['wind_speed']} mph"

        return weather

    def print_weather(self, city):
        weather = self.get_current_weather(city)
        if "error" in weather:
            print(weather["error"])
        else:
            print(f"{city}:")
            print(f"{weather['temperature']}, {weather['feels_like']}, {weather['weather_description']}")
            print(f"{weather['humidity']}%, {weather['wind_speed']}")

class Valves:
    def __init__(self):
        self.api_key = "your_openweather_api_key_here"
        self.units = "metric"  # or "imperial"
        self.language = "en"   # or "nl"