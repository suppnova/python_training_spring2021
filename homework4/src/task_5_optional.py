"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> print(list(fizzbuzz(5)))
['1', '2', 'fizz', '4', 'buzz']

>>> print(list(fizzbuzz(17)))
['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16', '17']

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator, List


def fizzbuzz(n: int) -> Generator[str, None, None]:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input number should be integer and not less than 0")
    for i in range(1, n + 1):
        yield "fizz" * (i % 3 == 0) + "buzz" * (i % 5 == 0) + str(i) * (
            i % 3 != 0 and i % 5 != 0
        )
