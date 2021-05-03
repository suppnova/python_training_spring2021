import pytest

from homework3.src.task04 import is_armstrong


@pytest.mark.parametrize(
    ["number", "expected_result"],
    [(0, True), (-1, False), (9, True), (10, False), (153, True)],
)
def test_is_armstrong(number: int, expected_result: bool):
    actual_result = is_armstrong(number)

    assert actual_result is expected_result
