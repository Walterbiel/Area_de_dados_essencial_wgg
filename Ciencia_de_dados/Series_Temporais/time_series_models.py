"""Modelos simples para séries temporais."""
from __future__ import annotations

from statistics import mean
from typing import Iterable, List


def moving_average_forecast(series: Iterable[float], window: int) -> List[float]:
    series_list = list(series)
    if window <= 0:
        raise ValueError("window must be positive")
    if window > len(series_list):
        raise ValueError("window must be smaller than the series length")
    forecasts: List[float] = []
    for end_idx in range(window, len(series_list) + 1):
        window_values = series_list[end_idx - window : end_idx]
        forecasts.append(round(mean(window_values), 2))
    return forecasts


def seasonal_index(series: Iterable[float], season_length: int) -> List[float]:
    values = list(series)
    if season_length <= 0:
        raise ValueError("season_length must be positive")
    if len(values) % season_length != 0:
        raise ValueError("Series length must be a multiple of season_length")
    num_seasons = len(values) // season_length
    indexes: List[float] = []
    for i in range(season_length):
        seasonal_values = [values[j * season_length + i] for j in range(num_seasons)]
        overall_avg = mean(values)
        indexes.append(round(mean(seasonal_values) / overall_avg, 2))
    return indexes
