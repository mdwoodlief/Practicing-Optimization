import pytest
from twttr import shorten


def test_low_shorten():
    assert shorten("something") == "smthng"


def test_cap_shorten():
    assert shorten("SOMETHING") == "SMTHNG"


def test_int():
    assert shorten("something1") == "smthng1"


def test_punc():
    assert shorten("some.") == "sm."
