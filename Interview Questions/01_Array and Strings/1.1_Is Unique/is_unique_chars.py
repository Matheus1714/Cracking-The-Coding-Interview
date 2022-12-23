import unittest

def is_unique_chars(s:str):
    if len(s) > 128:
        return False

    char_set = 128 * [False]
    for ch in s:
        i = ord(ch)
        if char_set[i]:
            return False
        char_set[i] = True

    return True

class Test(unittest.TestCase):
    dataT = [('a'), ('12'), ('123'), ('abcd'), ('s4fad'), ('')]
    dataF = [('1234562'), ('123123'), ('23ds2'), ('hb 627jh=j ()')]

    def test_is_unique_chars(self):

        for test_string in self.dataT:
            actual = is_unique_chars(test_string)
            self.assertTrue(actual)

        for test_string in self.dataF:
            actual = is_unique_chars(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
