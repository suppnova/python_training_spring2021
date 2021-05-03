from unittest.mock import Mock

from homework2.src.hw4 import cache


def test_cache():
    func = Mock()
    cached_func = cache(func)
    cached_func()
    cached_func()
    cached_func()

    assert func.call_count == 1
