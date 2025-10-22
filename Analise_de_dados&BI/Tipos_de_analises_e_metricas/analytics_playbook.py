"""Classificação de análises e métricas de negócio."""

from dataclasses import dataclass
from typing import Callable, Dict, Iterable, List


@dataclass(frozen=True)
class Metric:
    name: str
    description: str
    category: str


ANALYSIS_TYPES: Dict[str, str] = {
    "descritiva": "Entende o que aconteceu através de métricas históricas.",
    "diagnostica": "Investiga porque os eventos aconteceram.",
    "preditiva": "Estima resultados futuros com base no histórico.",
    "prescritiva": "Recomenda ações para atingir objetivos.",
}


def filter_metrics(metrics: Iterable[Metric], *, category: str) -> List[Metric]:
    """Retorna apenas métricas de uma categoria específica."""

    return [metric for metric in metrics if metric.category == category]


def build_dashboard(metrics: Iterable[Metric], formatter: Callable[[Metric], str]) -> List[str]:
    """Aplica um formatter para gerar descrições exibíveis em dashboards."""

    return [formatter(metric) for metric in metrics]
