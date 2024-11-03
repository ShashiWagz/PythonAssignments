import requests

API_Key = "0eddfdca9755df63b6bd572e3fa1cb14"

# Get city from user
city = input("Enter the name of the city: ")

# API request URL using city name
request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}"

try:
    response = requests.get(request_url)
    response.raise_for_status()  # Raises an HTTPError if the response code is not 200 (OK)

    # Parse the JSON response
    weather = response.json()

    # Get location and temperature (converting from Kelvin to Celsius)
    location = weather.get("name", "Unknown location")
    temperature_kelvin = weather["main"]["temp"]
    temperature_celsius = temperature_kelvin - 273.15  # Convert to Celsius

    # Print the location and temperature
    print(f"Location: {location}")
    print(f"Temperature: {temperature_celsius:.2f} °C")

except requests.exceptions.HTTPError as error:
    print(f"HTTP error occurred: {error}")
except requests.exceptions.RequestException as error:
    print(f"Request could not be completed: {error}")
except KeyError:
    print("Error: Could not find weather information for this location.")
