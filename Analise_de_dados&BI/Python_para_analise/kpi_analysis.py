"""Ferramentas para cálculo de métricas de vendas."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Iterable, List


@dataclass(frozen=True)
class SaleRecord:
    """Representa uma linha de venda utilizada pelos KPIs."""

    month: str
    customer_segment: str
    revenue: float
    transactions: int


def revenue_by_segment(records: Iterable[SaleRecord]) -> Dict[str, float]:
    """Calcula a receita total por segmento de cliente."""

    totals: Dict[str, float] = defaultdict(float)
    for record in records:
        totals[record.customer_segment] += record.revenue
    return dict(totals)


def monthly_average_ticket(records: Iterable[SaleRecord]) -> Dict[str, float]:
    """Retorna o ticket médio mensal para as vendas informadas."""

    totals: Dict[str, List[float]] = defaultdict(lambda: [0.0, 0.0])
    for record in records:
        totals[record.month][0] += record.revenue
        totals[record.month][1] += record.transactions

    average_ticket: Dict[str, float] = {}
    for month, (revenue_sum, transaction_sum) in totals.items():
        if transaction_sum == 0:
            average_ticket[month] = 0.0
        else:
            average_ticket[month] = round(revenue_sum / transaction_sum, 2)
    return average_ticket


def growth_rate(current_value: float, previous_value: float) -> float:
    """Calcula a taxa de crescimento percentual entre dois períodos."""

    if previous_value == 0:
        raise ValueError("previous_value must be non-zero to compute growth")
    return round(((current_value - previous_value) / previous_value) * 100, 2)
