"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import defaultdict
from operator import itemgetter
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
    return [
        word for word, _ in sorted(words.items(), key=itemgetter(1), reverse=True)[:10]
    ]


def count_symbols(file_path: str) -> Dict[str, int]:
    symbols = defaultdict(int)
    for line in read_by_line(file_path):
        for symbol in line:
            symbols[symbol] += 1
    return symbols


def get_rarest_char(file_path: str) -> str:
    symbols = count_symbols(file_path)
    return min(symbols.items(), key=lambda item: item[1])[0]


def count_punctuation_chars(file_path: str) -> int:
    counter = 0
    for symbol, amount in count_symbols(file_path).items():
        if symbol in punctuation:
            counter += amount
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    counter = 0
    for symbol, amount in count_symbols(file_path).items():
        if not symbol.isascii():
            counter += amount
    return counter


def get_most_common_non_ascii_char(file_path: str) -> Optional[str]:
    amount, char = 0, None
    for symbol, count in count_symbols(file_path).items():
        if not symbol.isascii() and count > amount:
            amount = count
            char = symbol
    return char
