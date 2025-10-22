"""Implementação simples de regressão linear multivariada."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List


@dataclass
class LinearRegressionModel:
    learning_rate: float = 0.01
    n_iterations: int = 1_000
    weights_: List[float] = field(default_factory=list)
    bias_: float = 0.0

    def fit(self, features: Iterable[Iterable[float]], targets: Iterable[float]) -> None:
        x = [list(row) for row in features]
        y = list(targets)
        if not x or not y:
            raise ValueError("Training data cannot be empty")
        if len(x) != len(y):
            raise ValueError("Features and targets must have same length")
        n_samples = len(x)
        n_features = len(x[0])
        self.weights_ = [0.0] * n_features
        self.bias_ = 0.0

        for _ in range(self.n_iterations):
            for i in range(n_samples):
                prediction = self._predict_row(x[i])
                error = prediction - y[i]
                for j in range(n_features):
                    self.weights_[j] -= self.learning_rate * error * x[i][j]
                self.bias_ -= self.learning_rate * error

    def _predict_row(self, row: Iterable[float]) -> float:
        return sum(weight * value for weight, value in zip(self.weights_, row)) + self.bias_

    def predict(self, features: Iterable[Iterable[float]]) -> List[float]:
        if not self.weights_:
            raise ValueError("Model must be fitted before prediction")
        return [self._predict_row(row) for row in features]
