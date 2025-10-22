from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType


def load_module(module_name: str, relative_path: str) -> ModuleType:
    repo_root = Path(__file__).resolve().parents[1]
    file_path = repo_root / relative_path
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot import module from {file_path}")
    module = importlib.util.module_from_spec(spec)
    import sys

    sys.modules[module_name] = module
    spec.loader.exec_module(module)  # type: ignore[assignment]
    return module
