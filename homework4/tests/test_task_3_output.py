from homework4.src.task_3_get_print_output import my_precious_logger


def test_my_precious_logger_err(capsys):
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.out == ""


def test_my_precious_logger_out(capsys):
    my_precious_logger("OK")
    captured = capsys.readouterr()
    assert captured.err == ""
