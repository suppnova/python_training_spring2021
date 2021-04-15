"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

Detailed instruction how to run doctests:
 - Install Python 3.9 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository https://github.com/suppnova/python_training_spring_2021
 - Checkout branch homework-4
 - Open terminal
 - Open directory with file task_4_doctest.py
 - Type 'python -m doctest -v task_4_doctest.py' in terminal

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


>>> fizzbuzz(5)
['1', '2', 'fizz', '4', 'buzz']

>>> fizzbuzz(17)
['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16', '17']

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input number should be integer and not less than 0")
    fizz_buzz_numbers = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            fizz_buzz_numbers.append("fizzbuzz")
        elif i % 3 == 0:
            fizz_buzz_numbers.append("fizz")
        elif i % 5 == 0:
            fizz_buzz_numbers.append("buzz")
        else:
            fizz_buzz_numbers.append(str(i))
    return fizz_buzz_numbers
