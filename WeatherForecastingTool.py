import requests
import json

def get_weather_forecast(city_name):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather?id=524901&appid=YOUR_API_KEY"

    try:
        response = requests.get(base_url, params={'q': city_name, 'appid': api_key})
        response.raise_for_status()
        weather_data = response.json()

        if 'main' in weather_data and 'temp' in weather_data['main']:
            temperature = weather_data['main']['temp']
            print(f"Temperature: {temperature} K")

        if 'main' in weather_data and 'humidity' in weather_data['main']:
            humidity = weather_data['main']['humidity']
            print(f"Humidity: {humidity}%")

        if 'weather' in weather_data and weather_data['weather']:
            weather_description = weather_data['weather'][0].get('description')
            print(f"Description: {weather_description}")

    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    except KeyError as err:
        print(f"Invalid response format: {err}")
    except json.JSONDecodeError as err:
        print(f"Unable to parse response: {err}")


city = input("Enter Ciyt name please: ")
get_weather_forecast(city)

