import pytest

from homework9.src.hw2 import Suppressor, suppressor


def test_positive_suppress_index_error():
    with Suppressor(IndexError):
        _ = [][2]


def test_suppressor_negative_test():
    with pytest.raises(IndexError):
        with Suppressor(ValueError):
            _ = [][2]


def test_suppress():
    with suppressor(AssertionError):
        assert 1 == 2


def test_suppress_negative():
    with pytest.raises(IndexError):
        with suppressor(AssertionError):
            _ = [][2]
