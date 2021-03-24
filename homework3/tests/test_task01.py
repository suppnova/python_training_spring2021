from homework3.src.task01 import func


def test_cached_func():
    first_call = func(100, 200)
    second_call = func(100, 200)
    _ = func(100, 200)

    fourth_call = func(100, 200)

    assert first_call is second_call and first_call is not fourth_call
