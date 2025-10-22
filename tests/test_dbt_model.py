from __future__ import annotations

from pathlib import Path


def test_dbt_model_contains_jinja_ref():
    root = Path(__file__).resolve().parents[1]
    sql_text = (root / "Engenharia_de_dados/dbt-databuildtool/models/dim_customers.sql").read_text(encoding="utf-8")
    assert "{{ ref('stg_customers') }}" in sql_text
    assert "INITCAP" in sql_text
