"""Funções utilitárias para preparação de dados."""
from __future__ import annotations

from typing import Iterable, List, Sequence, Tuple


def min_max_scale(column: Sequence[float]) -> List[float]:
    if not column:
        raise ValueError("column must not be empty")
    min_value = min(column)
    max_value = max(column)
    if min_value == max_value:
        return [0.0 for _ in column]
    return [(value - min_value) / (max_value - min_value) for value in column]


def train_test_split(dataset: Sequence[Tuple], test_ratio: float = 0.2) -> Tuple[List[Tuple], List[Tuple]]:
    if not 0 < test_ratio < 1:
        raise ValueError("test_ratio must be between 0 and 1")
    cutoff = int(len(dataset) * (1 - test_ratio))
    train = list(dataset[:cutoff])
    test = list(dataset[cutoff:])
    return train, test


def encode_categories(values: Iterable[str]) -> Tuple[List[int], dict]:
    mapping = {}
    encoded = []
    for value in values:
        if value not in mapping:
            mapping[value] = len(mapping)
        encoded.append(mapping[value])
    return encoded, mapping
