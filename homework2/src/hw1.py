"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

from string import punctuation
from typing import Dict, List, Optional


def read_by_line(file_name: str) -> str:
    with open(file_name, encoding="utf-8") as fi:
        for line in fi:
            bytes_str = line.encode("utf-8")
            yield bytes_str.decode("unicode-escape")


def get_longest_diverse_words(file_path: str) -> List[str]:
    words = dict()
    for line in read_by_line(file_path):
        for word in line.split():
            word = word.strip(punctuation)
            words[word] = len(set(word))
    return sorted(words, key=words.__getitem__, reverse=True)[:10]


def count_symbols(file_path: str) -> Dict[str, int]:
    symbols = {}
    for line in read_by_line(file_path):
        for symbol in line:
            if symbol not in symbols:
                symbols[symbol] = 1
            else:
                symbols[symbol] += 1
    return symbols


def get_rarest_char(file_path: str) -> str:
    symbols = count_symbols(file_path)
    return min(symbols.items(), key=lambda item: item[1])[0]


def count_punctuation_chars(file_path: str) -> int:
    counter = 0
    symbols = count_symbols(file_path)
    for symbol in symbols:
        if symbol in punctuation:
            counter += symbols[symbol]
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    counter = 0
    symbols = count_symbols(file_path)
    for symbol in symbols:
        if not symbol.isascii():
            counter += symbols[symbol]
    return counter


def get_most_common_non_ascii_char(file_path: str) -> Optional[str]:
    amount = 0
    symbols = count_symbols(file_path)
    for symbol in symbols:
        if not symbol.isascii() and symbols[symbol] > amount:
            amount = symbols[symbol]
            char = symbol
    if amount == 0:
        return None
    return char
