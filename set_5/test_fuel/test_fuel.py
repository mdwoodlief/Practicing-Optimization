import pytest
from fuel import convert
from fuel import gauge


def test_convert():
    assert convert("1/4") == 25


def test_error():
    with pytest.raises(ValueError):
        convert("h/h")
    with pytest.raises(ValueError):
        convert("1/h")
    with pytest.raises(ValueError):
        convert("h/1")
    with pytest.raises(ValueError):
        convert("3/1")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_perc():
    assert gauge(25) == "25%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
