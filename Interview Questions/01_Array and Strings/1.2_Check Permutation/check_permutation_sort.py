import unittest

def sort(s:str)->str:
    chs = list(s)
    chs.sort()
    return ''.join(chs)

def check_permutaton(s, t):

    if len(s) != len(t):
        return False
    return sort(s) == sort(t)

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