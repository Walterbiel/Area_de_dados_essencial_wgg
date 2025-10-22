"""Estrutura simplificada para simular tópicos Kafka em memória."""
from __future__ import annotations

from collections import defaultdict, deque
from typing import Deque, Dict, List


class InMemoryKafka:
    def __init__(self) -> None:
        self._topics: Dict[str, Deque[str]] = defaultdict(deque)

    def produce(self, topic: str, message: str) -> None:
        self._topics[topic].append(message)

    def consume(self, topic: str, batch_size: int = 1) -> List[str]:
        batch: List[str] = []
        queue = self._topics[topic]
        for _ in range(min(batch_size, len(queue))):
            batch.append(queue.popleft())
        return batch
