from __future__ import annotations

from tests.utils import load_module

kafka_module = load_module("in_memory_kafka", "Engenharia_de_dados/Kafka/in_memory_kafka.py")


def test_produce_and_consume_messages():
    broker = kafka_module.InMemoryKafka()
    broker.produce("events", "message-1")
    broker.produce("events", "message-2")
    assert broker.consume("events", batch_size=2) == ["message-1", "message-2"]
    assert broker.consume("events", batch_size=1) == []
