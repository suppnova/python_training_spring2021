from os import path

import pytest

from homework4.src.task_1_read_file import read_magic_number


@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (path.join(path.dirname(__file__), "int_positive_test_file.txt"), True),
        (path.join(path.dirname(__file__), "int_negative_test_file.txt"), False),
        (path.join(path.dirname(__file__), "float_test_file.txt"), True),
        (path.join(path.dirname(__file__), "complex_test_file.txt"), False),
    ],
)
def test_read_magic_number(file_path: str, expected_result: bool):
    actual_result = read_magic_number(file_path)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    "file_path",
    [
        path.join(path.dirname(__file__), "str_test_file.txt"),
        path.join(path.dirname(__file__), "empty_test_file.txt"),
        path.join(path.dirname(__file__), "nonexistent_test_file.txt"),
    ],
)
def test_read_number_for_value_error(file_path: str):
    with pytest.raises(ValueError):
        read_magic_number(file_path)
