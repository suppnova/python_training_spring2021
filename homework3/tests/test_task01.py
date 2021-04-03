from unittest.mock import Mock

from homework3.src.task01 import cache


def test_cached_func():
    func = Mock()
    cached_func = cache(times=2)(func)
    cached_func()
    cached_func()
    cached_func()
    assert func.call_count == 1
    cached_func()
    assert func.call_count == 2
