import requests
api_key = "882cb8372905d3f17b320f63e652cedf"
api_request = f"http://api.weatherstack.com/current?access_key={api_key}&query=Madrid"

def fetch_data():
    print("Fetching weather data from Weatherstack API.")
    try:
        response = requests.get(api_request)
        response.raise_for_status()
        print("API response received successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error has occurred: {e}")
        raise

#fetch_data()

def fake_fetch_data():
    response = {'request': {'type': 'City', 'query': 'Madrid, Spain', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Madrid', 'country': 'Spain', 'region': 'Madrid', 'lat': '40.400', 'lon': '-3.683', 'timezone_id': 'Europe/Madrid', 'localtime': '2025-10-29 20:29', 'localtime_epoch': 1761769740, 'utc_offset': '1.0'}, 'current': {'observation_time': '07:29 PM', 'temperature': 12, 'weather_code': 248, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0007_fog.png'], 'weather_descriptions': ['Patches Of Fog'], 'astro': {'sunrise': '07:41 AM', 'sunset': '06:15 PM', 'moonrise': '02:38 PM', 'moonset': 'No moonset', 'moon_phase': 'First Quarter', 'moon_illumination': 43}, 'air_quality': {'co': '183.85', 'no2': '57.25', 'o3': '3', 'so2': '5.55', 'pm2_5': '10.05', 'pm10': '11.95', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 4, 'wind_degree': 25, 'wind_dir': 'NNE', 'pressure': 1010, 'precip': 0, 'humidity': 94, 'cloudcover': 25, 'feelslike': 13, 'uv_index': 0, 'visibility': 3, 'is_day': 'no'}}
    return response

#fake_fetch_data()