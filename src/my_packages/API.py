import requests # For å gjøre HTTP-forespørsler til API
import os # For å jobbe med miljøvariabler og filsystem
from dotenv import load_dotenv  # For å laste miljøvariabler fra .env-fil

# Load environment variables
load_dotenv() # Laster variabler fra .env-fil

api_key = os.getenv('API_KEY') # Henter API-nøkkel fra miljøvariabler
city = 'Trondheim'  # Byen vi ønsker værdata for

try:
    # Build URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    print("API_KEY:", os.getenv("API_KEY"))  # Skal printe nøkkelen din
    
    # Make API request
    response = requests.get(url)
    response.raise_for_status()  # Gir feilmelding ved HTTP-feil
    
    data = response.json() # Konverterer JSON-svar til Python-dictionary
    
    # Extract data with error handling
    humidity = data['main']['humidity']     # Luftfuktighet i prosent
    pressure = data['main']['pressure']     # Lufttrykk i hPa
    wind = data['wind']['speed']            # Vindhastighet i m/s    
    description = data['weather'][0]['description'] # Vindhastighet i m/s
    temp = data['main']['temp']             # Temperatur i °C
    
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
