from homework3.src.task02 import main


def test_multiprocessing_calc_result_ten_numbers():
    actual_result, time = main()
    assert actual_result == 21846
