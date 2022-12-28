import unittest

def check_permutaton(s:str, t:str)->bool:

    if len(s) != len(t):
        return False

    letters = [0 for _ in range(128)]

    for c in s:
        letters[ord(c)] += 1
    
    for c in t:
        letters[ord(c)] -= 1
        if letters[ord(c)] < 0:
            return False
    
    return True

class Test(unittest.TestCase):
    
    def test_differents_lengths(self):
        s1 = 'abc'
        s2 = 'abcd'
        self.assertFalse(check_permutaton(s1, s2))
    
    def test_permutation(self):
        s1 = 'abc'
        s2 = 'cba'
        self.assertTrue(check_permutaton(s1, s2))
    
    def test_long_permutation(self):
        s1 = 'abc'
        s2 = 'abcd'
        self.assertFalse(check_permutaton(s1, s2))
    
    def test_permutation_same_set(self):
        s1 = 'abcabd'
        s2 = 'bcacdd'
        self.assertFalse(check_permutaton(s1, s2))

if __name__ == "__main__":
    unittest.main()