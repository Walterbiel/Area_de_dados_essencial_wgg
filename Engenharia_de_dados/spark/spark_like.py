"""Transformações inspiradas em Spark utilizando Python puro."""
from __future__ import annotations

from typing import Callable, List, Sequence


class DataFrame:
    def __init__(self, rows: Sequence[dict]):
        self._rows = [dict(row) for row in rows]

    def filter(self, predicate: Callable[[dict], bool]) -> "DataFrame":
        return DataFrame([row for row in self._rows if predicate(row)])

    def select(self, *columns: str) -> "DataFrame":
        return DataFrame([{column: row[column] for column in columns} for row in self._rows])

    def collect(self) -> List[dict]:
        return [dict(row) for row in self._rows]
