import pytest
from palindrome_permutation import verify_polindrome

def test_book_example():
    s = 'tact coa'
    assert verify_polindrome(s) == True