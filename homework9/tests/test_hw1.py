from typing import List

import pytest

from homework9.src.hw1 import merge_sorted_files


@pytest.mark.parametrize(
    ["file1_content", "file2_content", "expected_result"],
    [
        ("1\n3\n4", "2\n3\n6", [1, 2, 3, 3, 4, 6]),
        ("-3\n-1\n4", "-6\n0\n3", [-6, -3, -1, 0, 3, 4]),
        ("", "7", [7]),
    ],
)
def test_merge_sorted_files(
    file1_content: str, file2_content: str, expected_result: List, tmpdir
):
    tf1 = tmpdir.join("tf1.txt")
    tf1.write(file1_content)
    tf2 = tmpdir.join("tf2.txt")
    tf2.write(file2_content)
    actual_result = list(merge_sorted_files([tf1, tf2]))
    assert actual_result == expected_result


def test_merge_sorted_files_not_existing_file():
    with pytest.raises(FileNotFoundError):
        list(merge_sorted_files(["not_existing_files.txt", "file.txt"]))


def test_merge_sorted_files_with_not_int_values(tmpdir):
    with pytest.raises(ValueError):
        tf1 = tmpdir.join("tf1.txt")
        tf1.write("zzz")
        tf2 = tmpdir.join("tf2.txt")
        tf2.write("two")
        list(merge_sorted_files([tf1, tf2]))
