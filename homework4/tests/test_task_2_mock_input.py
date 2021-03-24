from collections import namedtuple
from unittest.mock import patch

import pytest

from homework4.src.task_2_mock_input import count_dots_on_i


@pytest.mark.parametrize(
    ["data", "expected_result"], [("test_data_iiiii", 5), ("test_data", 0), ("", 0)]
)
def test_count_dots(data: str, expected_result: int):
    with patch("requests.get") as fake_get:
        FakeResponse = namedtuple("Response", ["text", "status"])
        fake_get.return_value = FakeResponse(text=data, status=200)
        assert count_dots_on_i("url") == expected_result


@pytest.mark.parametrize("url", [None, 10])
def test_count_dots_on_i_for_value_error(url: str):
    with pytest.raises(ValueError):
        count_dots_on_i(url)
