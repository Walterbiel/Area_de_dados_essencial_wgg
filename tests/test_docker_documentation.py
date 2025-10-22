from __future__ import annotations

from pathlib import Path


def test_docker_documentation_has_base_image():
    root = Path(__file__).resolve().parents[1]
    text = (root / "Engenharia_de_dados/docker/data_pipeline_container.md").read_text(encoding="utf-8")
    assert "FROM python:3.11-slim" in text
    assert "CMD" in text
