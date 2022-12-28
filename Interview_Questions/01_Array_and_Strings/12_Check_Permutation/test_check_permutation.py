import pytest
from check_permutation_sort import check_permutaton
    
def test_differents_lengths():
    s1 = 'abc'
    s2 = 'abcd'
    assert (check_permutaton(s1, s2)) == False

def test_permutation():
    s1 = 'abc'
    s2 = 'cba'
    assert check_permutaton(s1, s2) == True

def test_long_permutation():
    s1 = 'abc'
    s2 = 'abcd'
    assert (check_permutaton(s1, s2)) == False

def test_permutation_same_set():
    s1 = 'abcabd'
    s2 = 'bcacdd'
    assert (check_permutaton(s1, s2)) == False
