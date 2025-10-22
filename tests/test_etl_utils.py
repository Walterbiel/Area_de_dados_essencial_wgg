from __future__ import annotations

from tests.utils import load_module

etl_utils = load_module("etl_utils", "Engenharia_de_dados/Python_para_engenharia/etl_utils.py")


def test_deduplicate_records():
    records = [
        {"id": "1", "value": "a"},
        {"id": "2", "value": "b"},
        {"id": "1", "value": "c"},
    ]
    deduped = etl_utils.deduplicate_records(records, key="id")
    assert deduped == [{"id": "1", "value": "a"}, {"id": "2", "value": "b"}]


def test_enrich_with_defaults():
    records = [{"id": "1"}]
    enriched = etl_utils.enrich_with_defaults(records, defaults={"country": "PT"})
    assert enriched == [{"country": "PT", "id": "1"}]
