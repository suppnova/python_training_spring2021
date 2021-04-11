import pytest

from homework9.src.hw3 import universal_file_counter


def test_universal_file_counter_without_token(tmpdir):
    tmpdir.join("tf1.txt").write("1\n3\n4")
    assert universal_file_counter(tmpdir, ".txt") == 3


def test_universal_file_counter_with_tokenizer(tmpdir):
    tf = tmpdir.join("tf1.txt").write("1\n3 z\n4 4")
    assert universal_file_counter(tmpdir, ".txt", str.split) == 5


def test_universal_file_counter_no_existing_files(tmpdir):
    assert universal_file_counter(tmpdir, ".no.files", str.split) == 0
