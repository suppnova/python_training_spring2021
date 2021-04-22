"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

# >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import heapq
from pathlib import Path
from typing import Iterator, List, Union


def unpack_content(file):
    try:
        with open(file) as fi:
            return [int(data) for data in fi]
    except ValueError:
        raise ValueError(f"File {file} contains not integer value")
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file} not found")


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    gen_data_files = []
    for file in file_list:
        gen_data_files.append(unpack_content(file))
    yield from heapq.merge(*gen_data_files)
