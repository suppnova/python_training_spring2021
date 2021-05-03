import pytest

from homework4.src.task_5_optional import fizzbuzz


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [
        (5, ["1", "2", "fizz", "4", "buzz"]),
        (10, ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz"]),
        (0, []),
    ],
)
def test_fizzbuzz(number: int, expected_result: list):
    actual_result = list(fizzbuzz(number))
    assert actual_result == expected_result


def test_fizzbuzz_not_int_input():
    with pytest.raises(ValueError):
        list(fizzbuzz("a"))


def test_fizzbuzz_less_than_zero_input():
    with pytest.raises(ValueError):
        list(fizzbuzz(-1))
