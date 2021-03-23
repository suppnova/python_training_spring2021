"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Generator, Sequence


def fib_generator(start: int) -> Generator[int, None, None]:
    a, b = 0, 1
    while a < start:
        a, b = b, a + b
    while True:
        yield a
        a, b = b, a + b


def check_fib_sequence(data: Sequence[int]) -> bool:
    if len(data) == 0:
        return False
    for data_item, fib in zip(data, fib_generator(data[0])):
        if data_item != fib:
            return False
    return True
