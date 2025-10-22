"""Simulação de orquestração de pipeline CI/CD."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class PipelineStage:
    name: str
    command: str
    depends_on: List[str]


class Pipeline:
    def __init__(self, stages: List[PipelineStage]):
        self._stages = {stage.name: stage for stage in stages}

    def execution_plan(self) -> List[str]:
        plan: List[str] = []
        visited: Dict[str, bool] = {}

        def visit(stage_name: str) -> None:
            if visited.get(stage_name) is True:
                return
            if visited.get(stage_name) is False:
                raise ValueError("Cyclic dependency detected")
            visited[stage_name] = False
            stage = self._stages[stage_name]
            for dependency in stage.depends_on:
                if dependency not in self._stages:
                    raise KeyError(f"Stage '{dependency}' not found")
                visit(dependency)
            visited[stage_name] = True
            plan.append(stage.command)

        for stage in self._stages.values():
            visit(stage.name)
        return plan
