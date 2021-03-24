"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Iterable, List


def custom_range(iter_obj: Iterable, *args) -> List:
    args_len = len(args)
    if args_len == 1:
        stop = iter_obj.index(args[0])
        return [char for char in iter_obj[:stop]]
    if args_len == 2:
        start, stop = (iter_obj.index(x) for x in args)
        return [char for char in iter_obj[start:stop]]
    if args_len == 3:
        start, stop = (iter_obj.index(x) for x in args[:2])
        step = args[2]
        return [char for char in iter_obj[start:stop:step]]
