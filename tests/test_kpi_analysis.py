from __future__ import annotations

from tests.utils import load_module

kpi = load_module(
    "kpi_analysis",
    "Analise_de_dados&BI/Python_para_analise/kpi_analysis.py",
)


def test_revenue_by_segment():
    records = [
        kpi.SaleRecord(month="2024-01", customer_segment="enterprise", revenue=1000, transactions=10),
        kpi.SaleRecord(month="2024-01", customer_segment="midmarket", revenue=500, transactions=5),
        kpi.SaleRecord(month="2024-02", customer_segment="enterprise", revenue=800, transactions=8),
    ]
    result = kpi.revenue_by_segment(records)
    assert result == {"enterprise": 1800, "midmarket": 500}


def test_monthly_average_ticket():
    records = [
        kpi.SaleRecord(month="2024-01", customer_segment="enterprise", revenue=1000, transactions=10),
        kpi.SaleRecord(month="2024-01", customer_segment="midmarket", revenue=500, transactions=5),
        kpi.SaleRecord(month="2024-02", customer_segment="enterprise", revenue=800, transactions=8),
    ]
    assert kpi.monthly_average_ticket(records) == {"2024-01": 100.0, "2024-02": 100.0}


def test_growth_rate():
    assert kpi.growth_rate(120, 100) == 20.0


def test_growth_rate_zero_previous():
    try:
        kpi.growth_rate(120, 0)
    except ValueError as exc:
        assert "previous_value" in str(exc)
    else:
        raise AssertionError("Expected ValueError when previous value is zero")
