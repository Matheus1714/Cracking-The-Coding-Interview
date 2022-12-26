import unittest
import re

def replace_spaces(s:str, n:int, rt='%20'):
    s = s.strip()
    return re.sub('\s+', rt, s)

class Test(unittest.TestCase):

    def test_normal_case(self):
        s = 'Mr John Smith   '
        n = len(s)
        expeted = 'Mr%20John%20Smith'
        self.assertEqual(replace_spaces(s, n), expeted)
    
    def test_only_spaces(self):
        s = '   '
        n = len(s)
        expeted = ''
        self.assertEqual(replace_spaces(s, n), expeted)

    def test_diffetens_spaces(self):
        s = '  Mr    John      Smith   '
        n = len(s)
        expeted = 'Mr%20John%20Smith'
        self.assertEqual(replace_spaces(s, n), expeted)    

if __name__ == '__main__':
    unittest.main()