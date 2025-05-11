import requests
import os

API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if response.status_code == 200:
        return f"{data['name']}: {data['main']['temp']}°C, {data['weather'][0]['description']}"
    else:
        return data.get('message', 'Error fetching weather data')

if __name__ == '__main__':
    city = input('Enter city: ')
    print(get_weather(city))