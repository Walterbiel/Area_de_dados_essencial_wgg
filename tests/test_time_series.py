from __future__ import annotations

from tests.utils import load_module

models = load_module(
    "time_series_models",
    "Ciencia_de_dados/Series_Temporais/time_series_models.py",
)


def test_moving_average_forecast():
    series = [10, 20, 30, 40, 50]
    forecast = models.moving_average_forecast(series, window=3)
    assert forecast == [20.0, 30.0, 40.0]


def test_seasonal_index():
    series = [10, 20, 30, 40, 50, 60]
    indexes = models.seasonal_index(series, season_length=3)
    assert indexes == [0.71, 1.0, 1.29]
