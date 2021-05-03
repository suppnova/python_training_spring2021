from typing import Any

import pytest

from homework4.src.task_3_get_print_output import my_precious_logger


@pytest.mark.parametrize(
    ["input_", "err", "out"],
    [
        ("error: file not found", "error: file not found\n", ""),
        ("OK", "", "OK\n"),
        ("ERROR", "", "ERROR\n"),
        ("e r r o r", "", "e r r o r\n"),
        ("don't start with error", "", "don't start with error\n"),
    ],
)
def test_my_precious_logger(capsys, input_: Any, err: str, out: str):
    my_precious_logger(input_)
    captured = capsys.readouterr()
    assert captured.err == err
    assert captured.out == out


def test_my_precious_logger_not_str_input():
    with pytest.raises(ValueError):
        my_precious_logger(8)
