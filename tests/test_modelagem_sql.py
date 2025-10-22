from __future__ import annotations

import sqlite3
from pathlib import Path


def read_sql(relative_path: str) -> str:
    root = Path(__file__).resolve().parents[1]
    return (root / relative_path).read_text(encoding="utf-8")


def test_sales_star_schema_creates_tables():
    schema_sql = read_sql("Analise_de_dados&BI/Modelagem_de_bancodedados/sales_star_schema.sql")
    with sqlite3.connect(":memory:") as conn:
        conn.executescript(schema_sql)
        tables = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
            )
        }
        assert tables == {"dim_customer", "dim_date", "dim_product", "fact_sales"}
        views = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='view' ORDER BY name"
            )
        }
        assert "vw_revenue_by_category" in views
