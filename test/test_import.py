import pytest


def test_something():
    assert 1 == (2 - 1)


def test_something_else():
    assert 'Something here'


def test_list_is_empty():
    assert len([]) == 0

def test_that_will_fail():
    assert False, 'AAAAAAAAAAAAAAA'
