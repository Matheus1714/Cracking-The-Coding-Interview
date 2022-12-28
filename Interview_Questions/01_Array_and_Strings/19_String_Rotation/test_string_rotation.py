import pytest
from string_rotation import is_rotation


def test_book_example():
    s1 = 'waterbottle'
    s2 = 'erbottlewat'
    assert is_rotation(s1, s2) == True

def test_false_rotation():
    s1 = 'waterbottle'
    s2 = 'erbottlewta'
    assert is_rotation(s1, s2) == False
