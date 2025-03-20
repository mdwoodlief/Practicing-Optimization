import pytest
from bank import value


def test_cap():
    assert value("HELLO") == (0)
    assert value("HI") == (20)
    assert value("BYE") == (100)


def test_low():
    assert value("hello") == (0)
    assert value("hi") == (20)
    assert value("bye") == (100)


def test_num():
    assert value("123") == (100)


def test_symbol():
    assert value("@") == (100)
