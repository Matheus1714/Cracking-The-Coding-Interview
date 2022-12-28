from typing import List
import unittest
from random import randint

Matrix = List[List]

def rotate(matrix:Matrix)->bool:
    nrow = len(matrix)
    ncol = len(matrix[1])
    if nrow == 0 or nrow != ncol:
        return False
    
    n = nrow
    for layer in range(0, n//2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first ] = matrix[last][last - offset]
            matrix[last][last - offset ] = matrix[i][last]
            matrix[i][last ] = top
    return True

class Test(unittest.TestCase):

    def test_simple_example(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        expeted = True
        self.assertEqual(rotate(matrix), expeted)

if __name__ == '__main__':
    unittest.main()
