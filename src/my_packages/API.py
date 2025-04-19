import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv('API_KEY')
city = 'Trondheim'

try:
    # Build URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    print("API_KEY:", os.getenv("API_KEY"))  # Skal printe nøkkelen din
    
    # Make API request
    response = requests.get(url)
    response.raise_for_status()  # Raises exception for HTTP errors
    
    data = response.json()
    
    # Extract data with error handling
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    
    # Print formatted output
    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Wind: {wind} m/s")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {description.capitalize()}")
    ### -> Må ha flere variabler med informasjon på prosjektet (ikke bare vannføring)
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
except KeyError as e:
    print(f"Unexpected data format from API: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
