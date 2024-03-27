import os
from dotenv import load_dotenv
from pprint import pprint
import requests


load_dotenv()


def get_current_weather(city="Sofia"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()
    return weather_data


def main():
    city: str = os.getenv("CURRENT_CITY") if os.getenv("CURRENT_CITY") else "NA"
    # city: str = os.getenv("CURRENT_CITY")

    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)


if __name__ == "__main__":
    main()
