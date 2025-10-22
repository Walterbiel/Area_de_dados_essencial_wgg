from __future__ import annotations

from tests.utils import load_module

spark_like = load_module("spark_like", "Engenharia_de_dados/spark/spark_like.py")


def test_dataframe_filter_and_select():
    df = spark_like.DataFrame([
        {"city": "Lisbon", "sales": 100},
        {"city": "Porto", "sales": 80},
    ])
    result = df.filter(lambda row: row["sales"] >= 90).select("city").collect()
    assert result == [{"city": "Lisbon"}]
