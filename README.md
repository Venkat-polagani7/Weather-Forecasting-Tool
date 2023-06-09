## Weather Forecasting Tool
This command-line tool accepts a city's name as input and returns the current weather forecast. It leverages the OpenWeatherMap API to fetch weather data and parses it using Python. The solution demonstrates how GitHub Copilot can assist in API usage, data parsing, and error handling.

## Prerequisites
Python 3.x installed on your machine.
requests library installed. You can install it by running pip install requests.
## Usage
Clone the repository or download the code files.

Obtain an API key from OpenWeatherMap by creating an account.

Replace "YOUR_API_KEY" in the weather_forecast.py script with your actual OpenWeatherMap API key.

Open a terminal or command prompt and navigate to the directory where the script is saved.

Run the script using the command python weather_forecast.py.

When prompted, enter the name of the city for which you want to retrieve the weather forecast.

The tool will send a request to the OpenWeatherMap API and display the current weather forecast for the specified city, including temperature, humidity, and weather description.

## How GitHub Copilot Assists
GitHub Copilot can provide suggestions and assistance in the following areas of the code:

API Usage: 
GitHub Copilot can suggest code snippets for making HTTP requests to the OpenWeatherMap API, including handling query parameters and API keys.

Data Parsing: 
Copilot can help with parsing the JSON response from the API, suggesting code for accessing nested data fields and handling missing or unexpected fields.

Error Handling: 
Copilot can provide suggestions for catching and handling various exceptions, such as network errors (requests.exceptions.RequestException), missing data fields (KeyError), and parsing errors (json.JSONDecodeError).

## OUTPUT
<img width="850" alt="image" src="https://github.com/Venkat-polagani7/Weather-Forecasting-Tool/assets/103422239/1f570ab9-80e0-4f65-85fe-34e729885103">

