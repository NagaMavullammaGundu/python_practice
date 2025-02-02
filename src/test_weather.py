"""Pytest for city weather"""

import weather
import pytest


def test_wrongcity_weather():
    city_name = "invalid city name"
    with pytest.raises(ValueError, match=f"Given city name {city_name} is invalid"):
        assert weather.city_weather(city_name)
