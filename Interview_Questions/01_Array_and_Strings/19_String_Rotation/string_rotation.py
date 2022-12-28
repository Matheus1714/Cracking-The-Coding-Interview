import unittest

def is_rotation(s0:str, s:str)->bool:
    if len(s0) != len(s):
        return False
    
    xy = s0
    yx = s
    xyxy = xy + xy
    return yx in xyxy
    
class Test(unittest.TestCase):

    def test_book_example(self):
        s1 = 'waterbottle'
        s2 = 'erbottlewat'
        self.assertTrue(is_rotation(s1, s2))
    
    def test_false_rotation(self):
        s1 = 'waterbottle'
        s2 = 'erbottlewta'
        self.assertFalse(is_rotation(s1, s2))

if __name__ == '__main__':
    unittest.main()