from homework5.src.save_original_info import custom_sum


def test_custom_sum_doc():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add__"


def test_custom_sum_name():
    assert custom_sum.__name__ == "custom_sum"


def test_custom_sum_original_func():
    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == 10
