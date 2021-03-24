"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.

Write a test for that function using pytest library.

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - all temporary files are removed after test run

You will learn:
 - how to test Exceptional cases
 - how to clean up after tests
 - how to check if file exists**
 - how to handle*** and raise**** exceptions in test. Use sample from the documentation.

* https://en.wikipedia.org/wiki/Interval_(mathematics)#Terminology
** https://docs.python.org/3/library/os.path.html
*** https://docs.python.org/3/tutorial/errors.html#handling-exceptions
**** https://docs.python.org/3/tutorial/errors.html#raising-exceptions
"""

from collections import namedtuple

CastResult = namedtuple("CastResult", ["status", "number"])


def in_interval(value):
    return 1 <= value < 3


def cast_to_complex(value):
    complex(value)


def cast_to_float(value):
    try:
        return CastResult(True, float(value))
    except ValueError:
        return CastResult(False, -1)


def read_magic_number(path: str) -> bool:
    try:
        with open(path, "r") as fi:
            first_line = fi.readline().strip()
            cast_to_complex(first_line)
            result, number = cast_to_float(first_line)
            return result and in_interval(number)
    except (ValueError, FileNotFoundError):
        raise ValueError
