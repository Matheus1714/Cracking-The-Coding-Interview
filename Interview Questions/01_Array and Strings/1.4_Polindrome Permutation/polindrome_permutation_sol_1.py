from typing import List
import unittest

def get_char_number(c:str)->str:
    a = ord('a')
    z = ord('z')
    val = ord(c)

    if a <= val and val <=z:
        return val - a
    return -1

def build_char_frequency_table(phrase:str)->List[int]:
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    for c in phrase:
        x = get_char_number(c)
        if x != -1:
            table[x] =+ 1
    return table

def check_max_one_odd(table:List[int])->bool:
    found_odd = False
    for count in table:
        if count%2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True

def is_permutation_of_palindrome(phrase:str)->bool:
    table = build_char_frequency_table(phrase)
    return check_max_one_odd(table)


class Test(unittest.TestCase):
    
    def test_book_example(self):
        s = 'tact coa'
        self.assertTrue(s)


if __name__ == '__main__':
    unittest.main()