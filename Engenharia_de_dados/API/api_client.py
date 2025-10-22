"""Cliente simplificado para consumo de APIs REST."""
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class WeatherReading:
    city: str
    temperature_c: float
    humidity: float

    @classmethod
    def from_payload(cls, payload: Dict[str, Any]) -> "WeatherReading":
        return cls(
            city=payload["city"],
            temperature_c=float(payload["temperature_c"]),
            humidity=float(payload["humidity"]),
        )


class WeatherAPIClient:
    """Processa respostas JSON e valida o schema básico."""

    def parse_response(self, response_text: str) -> WeatherReading:
        try:
            payload = json.loads(response_text)
        except json.JSONDecodeError as exc:
            raise ValueError("Invalid JSON payload") from exc

        required_fields = {"city", "temperature_c", "humidity"}
        if not required_fields.issubset(payload):
            missing = required_fields - payload.keys()
            raise ValueError(f"Missing fields: {', '.join(sorted(missing))}")
        return WeatherReading.from_payload(payload)
