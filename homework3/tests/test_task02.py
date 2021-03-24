from homework3.src.task02 import main

actual_result, actual_time = main()


def test_multiprocessing_calc_result():
    assert actual_result == 1025932


def test_multiprocessing_calc_time():
    assert actual_time <= 60
