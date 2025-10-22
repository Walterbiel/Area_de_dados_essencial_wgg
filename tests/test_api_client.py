from __future__ import annotations

from tests.utils import load_module

api_client = load_module("api_client", "Engenharia_de_dados/API/api_client.py")


def test_parse_response_success():
    payload = '{"city": "Lisbon", "temperature_c": 22.5, "humidity": 55}'
    reading = api_client.WeatherAPIClient().parse_response(payload)
    assert reading.city == "Lisbon"
    assert reading.temperature_c == 22.5


def test_parse_response_missing_fields():
    payload = '{"city": "Lisbon", "humidity": 55}'
    try:
        api_client.WeatherAPIClient().parse_response(payload)
    except ValueError as exc:
        assert "Missing fields" in str(exc)
    else:
        raise AssertionError("Expected ValueError for missing fields")
