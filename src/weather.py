import requests
import argparse


URL = "http://api.openweathermap.org/data/2.5/weather?"


def city_weather(city_name, units):
    api_key = "b3fcc4af13e5e9124f915c36d99ff956"

    complete_url = URL + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        print(f"City Name : {city_name}")
        # print(f"Minimum Temperature : {data['main']['temp_min']}K")
        # print(f"Maximum Temperature : {data['main']['temp_max']}K")
        pass
    else:
        raise ValueError(f"Given city name {city_name} is invalid")

    if units == "celsius":
        temperature_celsius(data["main"]["temp_min"], data["main"]["temp_max"])
    elif units == "farenheit":
        temperature_farenheit(data["main"]["temp_min"], data["main"]["temp_max"])


def temperature_celsius(temp_min, temp_max):
    temp_min_celsius = temp_min - 273.15
    temp_max_celsius = temp_max - 273.15

    print(f"Celsius Minimum Temperature : {temp_min_celsius} C")
    print(f"Celsius Maximum Temperature : {temp_max_celsius} C")


def temperature_farenheit(temp_min, temp_max):

    temp_min_farenheit = ((temp_min - 273.15) * (9 / 5)) + 32
    temp_max_farenheit = ((temp_max - 273.15) * (9 / 5)) + 32

    print(f"Farenheit Minimum Temperature : {temp_min_farenheit} F")
    print(f"Farenheit Maximum Temperature : {temp_max_farenheit} F")


def main():
    parser = argparse.ArgumentParser(description="Weather Report")
    parser.add_argument("--city_name", type=str, required=True, help="Name of the city")
    parser.add_argument(
        "--units",
        type=str,
        choices=["Celsius", "Farenheit"],
        default="Celsius",
        help="Temperature Units",
    )
    args = parser.parse_args()
    city_weather(args.city_name, args.units.lower())


if __name__ == "__main__":
    main()
