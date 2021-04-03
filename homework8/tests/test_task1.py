import pytest

from homework8.src.task1 import KeyValueStorage


def create_storage(file_text: str, tmpdir) -> KeyValueStorage:
    tmp_file = tmpdir.join("temp_file")
    tmp_file.write(file_text)
    return KeyValueStorage(tmp_file)


def test_keyvaluestorage_access_by_key(tmpdir):
    storage = create_storage(
        "name=kek\nlast_name=top\npower=9001\nsong=shadilay\n", tmpdir
    )
    assert storage["name"] == "kek"


def test_keyvaluestorage_access_by_attribute(tmpdir):
    storage = create_storage(
        "name=kek\nlast_name=top\npower=9001\nsong=shadilay\n", tmpdir
    )
    assert storage.song == "shadilay"
    assert storage.power == 9001


def test_keyvaluestorage_value_error(tmpdir):
    with pytest.raises(ValueError):
        create_storage("1name=kek", tmpdir)


def test_keyvaluestorage_attribute_error(tmpdir):
    with pytest.raises(AttributeError):
        storage = create_storage("name=kek", tmpdir)
        assert storage.song
