"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("pos_test_file.txt") as fi:
    for line in fi:
        ...

"""
import math
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    max_value, min_value = -math.inf, math.inf
    with open(file_name) as fi:
        for line in fi:
            current = int(line.rstrip())
            if current > max_value:
                max_value = current
            if current < min_value:
                min_value = current
    return min_value, max_value
