import pytest
from urlify import replace_spaces

def test_normal_case():
    s = 'Mr John Smith   '
    expeted = 'Mr%20John%20Smith'
    assert replace_spaces(s) == expeted

def test_only_spaces():
    s = '   '
    expeted = ''
    assert replace_spaces(s) == expeted

def test_diffetens_spaces():
    s = '  Mr    John      Smith   '
    expeted = 'Mr%20John%20Smith'
    assert replace_spaces(s) == expeted
