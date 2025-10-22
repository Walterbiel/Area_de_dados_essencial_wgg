"""Utilitários de transformação de dados para pipelines ETL."""
from __future__ import annotations

from typing import Dict, Iterable, List


def deduplicate_records(records: Iterable[Dict[str, str]], key: str) -> List[Dict[str, str]]:
    seen = set()
    unique_records = []
    for record in records:
        identifier = record[key]
        if identifier in seen:
            continue
        seen.add(identifier)
        unique_records.append(record)
    return unique_records


def enrich_with_defaults(records: Iterable[Dict[str, str]], defaults: Dict[str, str]) -> List[Dict[str, str]]:
    return [{**defaults, **record} for record in records]
