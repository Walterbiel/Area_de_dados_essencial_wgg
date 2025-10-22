"""Representação simplificada de um DAG Airflow."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class Task:
    task_id: str
    command: str
    downstream: List[str]


class Dag:
    def __init__(self, dag_id: str, tasks: List[Task]):
        self.dag_id = dag_id
        self._tasks: Dict[str, Task] = {task.task_id: task for task in tasks}

    def topological_order(self) -> List[str]:
        visited: Dict[str, bool] = {}
        order: List[str] = []

        def visit(task_id: str) -> None:
            if visited.get(task_id) is True:
                return
            if visited.get(task_id) is False:
                raise ValueError("Cycle detected in DAG")
            visited[task_id] = False
            task = self._tasks[task_id]
            for downstream in task.downstream:
                if downstream not in self._tasks:
                    raise KeyError(f"Task '{downstream}' not found")
                visit(downstream)
            visited[task_id] = True
            order.append(task_id)

        for task in self._tasks:
            visit(task)
        return order
