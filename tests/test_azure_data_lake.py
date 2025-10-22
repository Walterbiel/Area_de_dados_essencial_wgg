from __future__ import annotations

from datetime import datetime

from tests.utils import load_module

azure = load_module("data_lake", "Engenharia_de_dados/Azure/data_lake.py")


def test_data_lake_uri_format():
    path = azure.DataLakePath(
        container="datalake",
        layer="curated",
        dataset="sales",
        execution_date=datetime(2024, 5, 10),
    )
    assert (
        path.as_uri()
        == "https://storageaccount.dfs.core.windows.net/datalake/curated/sales/year=2024/month=05/day=10/"
    )
