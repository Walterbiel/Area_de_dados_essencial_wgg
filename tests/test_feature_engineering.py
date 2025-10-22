from __future__ import annotations

from tests.utils import load_module

features = load_module(
    "feature_engineering",
    "Ciencia_de_dados/Python_para_ciencia/feature_engineering.py",
)


def test_min_max_scale():
    scaled = features.min_max_scale([1, 2, 3])
    assert scaled == [0.0, 0.5, 1.0]


def test_train_test_split_ratio():
    data = list(range(10))
    train, test = features.train_test_split(data, test_ratio=0.3)
    assert len(train) == 7
    assert len(test) == 3


def test_encode_categories_produces_mapping():
    encoded, mapping = features.encode_categories(["a", "b", "a", "c"])
    assert encoded == [0, 1, 0, 2]
    assert mapping == {"a": 0, "b": 1, "c": 2}
