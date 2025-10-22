from __future__ import annotations

import sqlite3
from pathlib import Path


def read_sql(relative_path: str) -> str:
    root = Path(__file__).resolve().parents[1]
    return (root / relative_path).read_text(encoding="utf-8")


def setup_schema(conn: sqlite3.Connection) -> None:
    schema_sql = read_sql("Analise_de_dados&BI/Modelagem_de_bancodedados/sales_star_schema.sql")
    conn.executescript(schema_sql)
    conn.executemany(
        "INSERT INTO dim_product(product_id, product_name, category) VALUES (?, ?, ?)",
        [
            (1, "Notebook", "eletronicos"),
            (2, "Monitor", "eletronicos"),
            (3, "Cadeira", "escritorio"),
        ],
    )
    conn.executemany(
        "INSERT INTO dim_customer(customer_id, customer_name, segment) VALUES (?, ?, ?)",
        [
            (1, "Alice", "enterprise"),
            (2, "Bob", "midmarket"),
        ],
    )
    conn.executemany(
        "INSERT INTO dim_date(date_id, date_value, month, year) VALUES (?, ?, ?, ?)",
        [
            (1, "2024-01-01", 1, 2024),
            (2, "2024-01-02", 1, 2024),
        ],
    )
    conn.executemany(
        "INSERT INTO fact_sales(sale_id, date_id, customer_id, product_id, quantity, unit_price, discount)"
        " VALUES (?, ?, ?, ?, ?, ?, ?)",
        [
            (1, 1, 1, 1, 2, 2500.0, 0.1),
            (2, 1, 2, 2, 1, 1000.0, 0.0),
            (3, 2, 1, 3, 4, 300.0, 0.05),
        ],
    )


def test_revenue_by_category_query():
    queries = read_sql("Analise_de_dados&BI/SQL/retail_queries.sql").split(";\n\n")
    with sqlite3.connect(":memory:") as conn:
        setup_schema(conn)
        revenue_query = queries[0]
        rows = list(conn.execute(revenue_query))
        assert rows[0][0] == "eletronicos"
        assert round(rows[0][1], 2) == 5500.0


def test_average_ticket_query():
    queries = read_sql("Analise_de_dados&BI/SQL/retail_queries.sql").split(";\n\n")
    with sqlite3.connect(":memory:") as conn:
        setup_schema(conn)
        ticket_query = queries[1]
        rows = list(conn.execute(ticket_query))
        assert dict(rows) == {"enterprise": 940.0, "midmarket": 1000.0}
