import pytest
from src.decorators import log


def test_log():
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(6, 5)
    assert result == 11


def test_log_capsys(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(6, 5)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n\n"


def test_log_error():
    with pytest.raises(Exception):

        def my_function(x, y):
            return x + y

        my_function(6, "5")
