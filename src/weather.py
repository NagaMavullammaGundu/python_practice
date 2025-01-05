import requests

URL = "http://api.openweathermap.org/data/2.5/weather?"


def city_weather(city_name):
    api_key = "b3fcc4af13e5e9124f915c36d99ff956"

    complete_url = URL + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        print(f"City Name : {city_name}")
        print(f"Minimum Temperature : {data['main']['temp_min']} F")
        print(f"Maximum Temperature : {data['main']['temp_max']} F")
    else:
        raise ValueError(f"Given city name {city_name} is invalid")


def main():
    city_name = input("Enter the city name :")
    city_weather(city_name)


if __name__ == "__main__":
    main()
