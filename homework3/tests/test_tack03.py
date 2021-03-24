import pytest

from homework3.src.task03 import Filter, make_filter


def test_class_filter():
    expected_result = [2, 4, 6, 8]
    positive_even = Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    actual_result = positive_even.apply(range(-10, 10))
    assert actual_result == expected_result


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    {"0"},
    {"name": "polly"},
]


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ({"name": "polly", "type": "bird"}, [sample_data[1]]),
        ({"name": "polly"}, [sample_data[1], sample_data[3]]),
        ({"name": "Bill", "type": "bird"}, []),
    ],
)
def test_make_filter(value, expected_result):
    actual_result = make_filter(**value).apply(sample_data)

    assert actual_result == expected_result
