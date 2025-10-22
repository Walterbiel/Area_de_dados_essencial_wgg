"""Helpers para padronizar estruturas de Data Lake na Azure."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class DataLakePath:
    container: str
    layer: str
    dataset: str
    execution_date: datetime

    def as_uri(self) -> str:
        partition = self.execution_date.strftime("year=%Y/month=%m/day=%d")
        return f"https://storageaccount.dfs.core.windows.net/{self.container}/{self.layer}/{self.dataset}/{partition}/"
