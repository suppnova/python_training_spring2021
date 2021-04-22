"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

# For dir with two files from hw1.py:
# >>> universal_file_counter(os.path.dirname(__file__), "txt")
# 6
# >>> universal_file_counter(os.path.dirname(__file__), "txt", str.split)
# 6

"""
import os
from pathlib import Path
from typing import Callable, Optional


def count_lines(dir_path, file_name):
    lines = 0
    with open(os.path.join(dir_path, file_name)) as fi:
        lines += sum(1 for _ in fi)
    return lines


def count_tokens(dir_path, file_name, tokenizer):
    tokens = 0
    with open(os.path.join(dir_path, file_name)) as fi:
        for token in map(tokenizer, fi):
            tokens += sum(1 for _ in token)
    return tokens


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    lines_counter, tokens_counter = 0, 0
    for file in os.listdir(dir_path):
        if file.endswith(file_extension) and os.path.isfile(
            os.path.join(dir_path, file)
        ):
            if tokenizer:
                tokens_counter += count_tokens(dir_path, file, tokenizer)
            else:
                lines_counter += count_lines(dir_path, file)
    return lines_counter if lines_counter else tokens_counter
