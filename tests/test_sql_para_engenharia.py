from __future__ import annotations

import sqlite3
from pathlib import Path


def read_sql(relative_path: str) -> str:
    root = Path(__file__).resolve().parents[1]
    return (root / relative_path).read_text(encoding="utf-8")


def test_warehouse_transformations_view():
    sql_script = read_sql("Engenharia_de_dados/SQL_para_engenharia/warehouse_transformations.sql")
    with sqlite3.connect(":memory:") as conn:
        conn.executescript(sql_script)
        conn.executemany(
            "INSERT INTO stg_customers(customer_id, status, signup_date) VALUES (?, ?, ?)",
            [
                (1, "active", "2023-01-01"),
                (2, "inactive", "2023-02-01"),
            ],
        )
        conn.executemany(
            "INSERT INTO stg_usage(customer_id, month, consumption) VALUES (?, ?, ?)",
            [
                (1, "2024-01", 100),
                (1, "2024-02", 120),
                (2, "2024-01", 10),
            ],
        )
        rows = list(conn.execute("SELECT * FROM vw_churn_features ORDER BY customer_id"))
        assert rows == [
            (1, "active", 2, 110.0),
            (2, "inactive", 1, 10.0),
        ]
