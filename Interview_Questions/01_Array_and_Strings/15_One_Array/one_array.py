import unittest
from typing import List

def one_edit_replace(s1:str, s2:str)->bool:
    found_difference = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if found_difference:
                return False
            found_difference = True
    return True

def one_edit_insert(s1:str, s2:str)->bool:
    index1 = 0
    index2 = 0
    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

def one_edit_away(first:str, second:str)->bool:
    if len(first) == len(second):
        return one_edit_replace(first, second)
    elif len(first) + 1 == len(second):
        return one_edit_insert(first, second)
    elif len(first) - 1 == len(second):
        return one_edit_insert(second, first)
    return False

class Test(unittest.TestCase):
    
    def test_book_remove_between(self):
        original = 'pale'
        changed = 'ple'
        self.assertTrue(one_edit_away(original, changed))
    
    def test_book_remove_final(self):
        original = 'pales'
        changed = 'pale'
        self.assertTrue(one_edit_away(original, changed))
    
    def test_book_one_replace(self):
        original = 'pale'
        changed = 'bale'
        self.assertTrue(one_edit_away(original, changed))
    
    def test_book_two_replace(self):
        original = 'pale'
        changed = 'bake'
        self.assertFalse(one_edit_away(original, changed))
    
    def test_one_insert(self):
        original = 'pale'
        changed = 'pales'
        self.assertTrue(one_edit_away(original, changed))
    
    def test_two_insert(self):
        original = 'pale'
        changed = 'paless'
        self.assertFalse(one_edit_away(original, changed))


if __name__ == '__main__':
    unittest.main()

