import pytest

from homework7.src.hw2 import backspace_compare


@pytest.mark.parametrize(
    ["first_str", "second_str", "expected_result"],
    [
        ("", "", True),
        ("a#", "#", True),
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
    ],
)
def test_backspace_compare(first_str: str, second_str: str, expected_result: bool):
    assert backspace_compare(first_str, second_str) is expected_result
