import os
from typing import List

import pytest

from homework2.src.hw1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (
            os.path.join(os.path.dirname(__file__), "data.txt"),
            [
                "unmißverständliche",
                "Bevölkerungsabschub",
                "Kollektivschuldiger",
                "Werkstättenlandschaft",
                "Schicksalsfiguren",
                "politisch-strategischen",
                "Selbstverständlich",
                "résistance-Bewegungen",
                "Fingerabdrucks",
                "Friedensabstimmung",
            ],
        ),
        (
            os.path.join(os.path.dirname(__file__), "simple_data.txt"),
            [
                "simple_data",
                "punctuation",
                "non-ascii",
                "chars",
                "hello",
                "this",
                "file",
                "some",
                "only",
                "have",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(file_path: str, expected_result: List):
    actual_result = get_longest_diverse_words(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "data.txt"), "›"),
        (os.path.join(os.path.dirname(__file__), "simple_data.txt"), "f"),
    ],
)
def test_get_rarest_char(file_path: str, expected_result: str):
    actual_result = get_rarest_char(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "data.txt"), 5305),
        (os.path.join(os.path.dirname(__file__), "simple_data.txt"), 13),
    ],
)
def test_count_punctuation_chars(file_path: str, expected_result: int):
    actual_result = count_punctuation_chars(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "data.txt"), 2972),
        (os.path.join(os.path.dirname(__file__), "simple_data.txt"), 3),
    ],
)
def test_count_non_ascii_chars(file_path: str, expected_result: int):
    actual_result = count_non_ascii_chars(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (os.path.join(os.path.dirname(__file__), "data.txt"), "\u00e4"),
        (os.path.join(os.path.dirname(__file__), "simple_data.txt"), "\u00fc"),
    ],
)
def test_get_most_common_non_ascii_char(file_path: str, expected_result: str):
    actual_result = get_most_common_non_ascii_char(file_path)

    assert actual_result == expected_result
