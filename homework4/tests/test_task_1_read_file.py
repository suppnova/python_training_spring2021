import shutil
from os import path

import pytest

from homework4.src.task_1_read_file import read_magic_number


@pytest.mark.parametrize(
    ["file_name", "file_content", "expected_result"],
    [
        ("int_positive_test_file.txt", "2\n32", True),
        ("int_negative_test_file.txt", "32\n2", False),
        ("float_test_file.txt", "1.0", True),
        ("complex_test_file.txt", "5-2j", False),
    ],
)
def test_read_magic_number(
    tmpdir, file_name: str, file_content: str, expected_result: bool
):
    _ = tmpdir.join(file_name).write(file_content)
    actual_result = read_magic_number(path.join(tmpdir, file_name))
    shutil.rmtree(str(tmpdir))
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["file_name", "file_content"],
    [("str_test_file.txt", "Here's a string"), ("empty_test_file.txt", "")],
)
def test_read_magic_number_value_error(tmpdir, file_name: str, file_content: str):
    _ = tmpdir.join(file_name).write(file_content)
    with pytest.raises(ValueError):
        read_magic_number(path.join(tmpdir, file_name))
    shutil.rmtree(str(tmpdir))


def test_read_number_for_file_not_found_error(tmpdir):
    with pytest.raises(FileNotFoundError):
        read_magic_number(path.join(tmpdir, "nonexistent_test_file.txt"))
    shutil.rmtree(str(tmpdir))
