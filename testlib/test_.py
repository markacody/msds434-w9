import pytest


def test01():
    return 1


def test0a():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert x == y, "test failed"
