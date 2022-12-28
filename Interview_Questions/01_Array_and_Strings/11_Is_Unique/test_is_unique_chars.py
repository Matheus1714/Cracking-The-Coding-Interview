import pytest
from is_unique_chars import is_unique_chars

dataT = [('a'), ('12'), ('123'), ('abcd'), ('s4fad'), ('')]
dataF = [('1234562'), ('123123'), ('23ds2'), ('hb 627jh=j ()')]

def test_is_unique_chars_true():
    for test_string in dataT:
        actual = is_unique_chars(test_string)
        assert actual == True

def test_is_unique_chars_false():
    for test_string in dataF:
        actual = is_unique_chars(test_string)
        assert actual == False
    