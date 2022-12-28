import pytest
from string_compression import compress

def test_book_example():
    s = 'aabcccccaaa'
    expeted = 'a2b1c5a3'
    assert compress(s) == expeted

def test_not_compressed():
    s = 'abca'
    expeted = 'abca'
    assert compress(s) == expeted

def test_empty_string():
    s = ''
    expeted = ''
    assert compress(s) == expeted

def test_length_1():
    s = 'a'
    expeted = 'a'
    assert compress(s) == expeted
