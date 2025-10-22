from __future__ import annotations

from tests.utils import load_module

playbook = load_module(
    "analytics_playbook",
    "Analise_de_dados&BI/Tipos_de_analises_e_metricas/analytics_playbook.py",
)


def test_filter_metrics_by_category():
    metrics = [
        playbook.Metric("Net Revenue", "Receita líquida", "descritiva"),
        playbook.Metric("Churn", "Clientes perdidos", "diagnostica"),
    ]
    filtered = playbook.filter_metrics(metrics, category="descritiva")
    assert filtered == [metrics[0]]


def test_build_dashboard_formats_strings():
    metrics = [playbook.Metric("Churn", "Clientes perdidos", "diagnostica")]
    dashboard = playbook.build_dashboard(
        metrics,
        formatter=lambda m: f"{m.name}: {m.description}",
    )
    assert dashboard == ["Churn: Clientes perdidos"]


def test_analysis_types_dictionary_is_complete():
    assert set(playbook.ANALYSIS_TYPES) == {
        "descritiva",
        "diagnostica",
        "preditiva",
        "prescritiva",
    }
