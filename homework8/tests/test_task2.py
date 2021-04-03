import sqlite3

import pytest

from homework8.src.task2 import TableData

presidents = TableData(database_name="example.sqlite", table_name="presidents")


def test_len_tabledata():
    assert len(presidents) == 3


def test__access_by_key():
    assert presidents["Yeltsin"] == {"name": "Yeltsin", "age": 999, "country": "Russia"}


def test_tabledata_method_contains():
    assert "Yeltsin" in presidents and "Putin" not in presidents


def test_iteration_protocol():
    presidents_names = []
    total_age = 0
    for president in presidents:
        presidents_names.append(president["name"])
        total_age += president["age"]
    assert (
        presidents_names == ["Yeltsin", "Trump", "Big Man Tyrone"] and total_age == 2437
    )


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        TableData(database_name="notexist.sqlite", table_name="presidents")


def test_database_error():
    with pytest.raises(sqlite3.DatabaseError):
        TableData(database_name="example.sqlite", table_name="no_table")
