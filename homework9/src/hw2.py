"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with suppressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


class Suppressor(object):
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, ex_type, ex_value, tb):
        if ex_type is self.exception:
            return True


@contextmanager
def suppressor(exception):
    try:
        yield 3
    except exception:
        pass
    finally:
        pass
