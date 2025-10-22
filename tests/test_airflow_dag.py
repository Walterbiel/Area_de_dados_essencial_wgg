from __future__ import annotations

from tests.utils import load_module

airflow = load_module("dag_example", "Engenharia_de_dados/airflow/dag_example.py")


def test_topological_order_returns_dependencies_last():
    dag = airflow.Dag(
        dag_id="daily_ingestion",
        tasks=[
            airflow.Task("extract", "python extract.py", ["transform"]),
            airflow.Task("transform", "python transform.py", ["load"]),
            airflow.Task("load", "python load.py", []),
        ],
    )
    order = dag.topological_order()
    assert order[-1] == "extract"
    assert order[0] == "load"


def test_topological_order_cycle_detection():
    dag = airflow.Dag(
        dag_id="cycle",
        tasks=[
            airflow.Task("a", "echo a", ["b"]),
            airflow.Task("b", "echo b", ["a"]),
        ],
    )
    try:
        dag.topological_order()
    except ValueError as exc:
        assert "Cycle" in str(exc)
    else:
        raise AssertionError("Expected ValueError for cyclic DAG")
