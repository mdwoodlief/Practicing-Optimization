import pytest
from plates import is_valid


def test_two_letters():
    assert is_valid("aa1234") == True
    assert is_valid("aa") == True
    assert is_valid("a1") == None
    assert is_valid("11") == None
    assert is_valid("1a") == None


def test_len():
    assert is_valid("a") == None
    assert is_valid("1") == None
    assert is_valid("aa12345") == None


def test_mid():
    assert is_valid("aa1a") == None
    assert is_valid("aa1") == True


def test_firstnum():
    assert is_valid("aa0") == None
    assert is_valid("aa1") == True
    assert is_valid("aa10") == True


def test_punc():
    assert is_valid("aa!") == None
    assert is_valid("aa,") == None
    assert is_valid("aa aa") == None
