import pytest

from homework2.src.hw4 import cache


def func_values(a, b):
    return (a ** b) ** 2


def func_mutable(*args):
    return {*args}


@pytest.mark.parametrize(
    ["func", "values"],
    [
        (func_values, (3, 5)),
        (func_mutable, (10, 10, 5)),
    ],
)
def test_cache(func, values):
    cache_func = cache(func)

    val_1 = cache_func(*values)
    val_2 = cache_func(*values)

    assert val_1 is val_2
