import pytest
from one_array import one_edit_away
    
def test_book_remove_between():
    original = 'pale'
    changed = 'ple'
    assert one_edit_away(original, changed) == True

def test_book_remove_final():
    original = 'pales'
    changed = 'pale'
    assert one_edit_away(original, changed) == True

def test_book_one_replace():
    original = 'pale'
    changed = 'bale'
    assert one_edit_away(original, changed) == True

def test_book_two_replace():
    original = 'pale'
    changed = 'bake'
    assert one_edit_away(original, changed) == False

def test_one_insert():
    original = 'pale'
    changed = 'pales'
    assert one_edit_away(original, changed) == True

def test_two_insert():
    original = 'pale'
    changed = 'paless'
    assert one_edit_away(original, changed) == False
