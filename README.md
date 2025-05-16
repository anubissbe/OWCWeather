
🌤️ OWCWeather
==============

Overview
--------

**OWCWeather** is a simple Python application that fetches and displays current weather information for a specified city using the [OpenWeather API](https://openweathermap.org/api). It supports customizable units (metric/imperial) and language (English/Dutch), making it adaptable for different user preferences.

📌 Features
-----------

*   Real-time weather data (temperature, feels like, weather description, humidity, wind speed).
*   Customizable units: metric (°C, m/s) or imperial (°F, mph).
*   Language support: English (en) or Dutch (nl).

🧰 Prerequisites
----------------

*   Python 3.x
*   [requests](https://pypi.org/project/requests/) library

🚀 Installation
---------------

Install dependencies:

    pip install requests

🔧 Usage
--------

Example code:

    
    from OWCWeather import WeatherApp
    
    # Initialize the app
    app = WeatherApp()
    
    # Set your OpenWeather API key
    app.valves.api_key = "your_openweather_api_key_here"
    
    # Set units and language (optional)
    app.valves.units = "metric"  # or "imperial"
    app.valves.language = "en"   # or "nl"
    
    # Get and print weather
    app.print_weather("Amsterdam")
      

📝 Example Code
---------------

Complete example:

    
    from OWCWeather import WeatherApp
    
    # Initialize the app
    app = WeatherApp()
    
    # Set your API key
    app.valves.api_key = "your_openweather_api_key_here"
    
    # Set units and language
    app.valves.units = "metric"
    app.valves.language = "en"
    
    # Get and print weather
    app.print_weather("London")
      

🧰 Customization
----------------

*   Change units: Modify `app.valves.units` to `"imperial"` for Fahrenheit and mph.
*   Change language: Modify `app.valves.language` to `"nl"` for Dutch.

📌 Credits
----------

This project was created and maintained by [anubissbe](https://github.com/anubissbe).

You can find the source code on GitHub: [https://github.com/anubissbe/OWCWeather](https://github.com/anubissbe/OWCWeather).

🛠️ Contributing
----------------

*   Fork the repository and submit a pull request.
*   Report bugs or feature requests via the GitHub issue tracker.

📄 License
----------

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

📌 Notes
--------

*   Replace `"your_openweather_api_key_here"` with your actual API key.
*   The code uses the **UTC timezone** for time awareness.