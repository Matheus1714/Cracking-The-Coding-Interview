from typing import List
import unittest

def get_char_number(c:str)->str:
    a = ord('a')
    z = ord('z')
    val = ord(c)

    if a <= val and val <=z:
        return val - a
    return -1

def is_permutation_of_palindrome(phrase:str)->bool:
    count_odd = 0
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    for c in phrase:
        x = get_char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2 == 1:
                count_odd += 1
            else:
                table[x] -= 1
    return count_odd <= 1

class Test(unittest.TestCase):
    
    def test_book_example(self):
        s = 'tact coa'
        self.assertTrue(s)

if __name__ == '__main__':
    unittest.main()