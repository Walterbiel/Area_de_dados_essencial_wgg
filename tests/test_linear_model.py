from __future__ import annotations

from tests.utils import load_module

linear = load_module(
    "linear_model",
    "Ciencia_de_dados/Machine_Learning/linear_model.py",
)


def test_linear_regression_learns_simple_relationship():
    model = linear.LinearRegressionModel(learning_rate=0.01, n_iterations=2000)
    features = [[1], [2], [3], [4]]
    targets = [3, 5, 7, 9]  # y = 2x + 1
    model.fit(features, targets)
    predictions = model.predict([[5], [6]])
    assert all(abs(pred - expected) < 0.5 for pred, expected in zip(predictions, [11, 13]))


def test_predict_without_fit_raises():
    model = linear.LinearRegressionModel()
    try:
        model.predict([[1]])
    except ValueError as exc:
        assert "fitted" in str(exc)
    else:
        raise AssertionError("Expected ValueError when predicting without fitting")
