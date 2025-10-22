from __future__ import annotations

from tests.utils import load_module

pipeline_module = load_module("pipeline", "Engenharia_de_dados/CI-CD/pipeline.py")


def build_sample_pipeline():
    return pipeline_module.Pipeline(
        [
            pipeline_module.PipelineStage(name="test", command="pytest", depends_on=["lint"]),
            pipeline_module.PipelineStage(name="deploy", command="terraform apply", depends_on=["test"]),
            pipeline_module.PipelineStage(name="lint", command="ruff check", depends_on=[]),
        ]
    )


def test_execution_plan_resolves_dependencies():
    plan = build_sample_pipeline().execution_plan()
    assert plan == ["ruff check", "pytest", "terraform apply"]


def test_cycle_detection():
    pipeline = pipeline_module.Pipeline(
        [
            pipeline_module.PipelineStage(name="a", command="a", depends_on=["b"]),
            pipeline_module.PipelineStage(name="b", command="b", depends_on=["a"]),
        ]
    )
    try:
        pipeline.execution_plan()
    except ValueError as exc:
        assert "Cyclic" in str(exc)
    else:
        raise AssertionError("Expected ValueError for cyclic dependency")
