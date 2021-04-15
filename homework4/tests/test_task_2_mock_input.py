from collections import namedtuple
from unittest.mock import patch

import pytest
import requests

from homework4.src.task_2_mock_input import count_dots_on_i


@pytest.mark.parametrize(
    ["data", "expected_result"], [("test_data_iiiii", 5), ("test_data", 0), ("", 0)]
)
def test_count_dots(data: str, expected_result: int):
    with patch("requests.get") as fake_get:
        FakeResponse = namedtuple("Response", ["text", "status"])
        fake_get.return_value = FakeResponse(text=data, status=200)
        assert count_dots_on_i("url") == expected_result


def test_count_dots_on_i_connection_error():
    with pytest.raises(requests.exceptions.ConnectionError):
        count_dots_on_i("http://goglya.com")


def test_count_dots_on_i_missing_schema():
    with pytest.raises(requests.exceptions.MissingSchema):
        count_dots_on_i("google.com")
