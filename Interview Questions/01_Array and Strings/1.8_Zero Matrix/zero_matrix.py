import unittest
from typing import List, Tuple

MatrixMN = List[List]

def get_zeros_coord(matrix:MatrixMN, m:int, n:int)->List[Tuple[int, int]]:
    zeros = []
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                coord = (row, col)
                zeros.append(coord)
    return zeros

def nullify_row(matrix:MatrixMN, n:int, row:int)->MatrixMN:
    for i in range(n):
        matrix[row][i] = 0
    return matrix

def nullify_col(matrix:MatrixMN, m:int, col:int)->MatrixMN:
    for i in range(m):
        matrix[i][col] = 0
    return matrix

def get_zero_matrix(matrix:MatrixMN, m:int, n:int, zeros:List[Tuple[int, int]])->MatrixMN:
    for coord in zeros:
        row = coord[0]
        col = coord[1]
        matrix = nullify_row(matrix, n, row)
        matrix = nullify_col(matrix, m, col)
    return matrix

def zero_matrix(matrix:MatrixMN)->MatrixMN:
    M = len(matrix)
    N = len(matrix[0])
    zeros = get_zeros_coord(matrix, M, N)
    zero_matrix = get_zero_matrix(matrix, M, N, zeros)
    return zero_matrix
    
class Test(unittest.TestCase):

    def test_simple_example(self):
        matrix = [
            [1, 2, 3, 4, 1, 4, 1, 3],
            [0, 2, 3, 4, 1, 0, 2, 3],
            [3, 1, 2, 3, 4, 5, 1, 2],
            [1, 2, 3, 4, 4, 5, 2, 1],
            [3, 4, 5, 6, 7, 3, 5, 1],
            [1, 2, 4, 3, 1, 2, 4, 5],
            [1, 1, 2, 3, 4, 5, 4, 2],
            [1, 2, 4, 5, 2, 1, 2, 4],
        ]
        expeted = [
            [0, 2, 3, 4, 1, 0, 1, 3],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 2, 3, 4, 0, 1, 2],
            [0, 2, 3, 4, 4, 0, 2, 1],
            [0, 4, 5, 6, 7, 0, 5, 1],
            [0, 2, 4, 3, 1, 0, 4, 5],
            [0, 1, 2, 3, 4, 0, 4, 2],
            [0, 2, 4, 5, 2, 0, 2, 4],
        ]
        self.assertEqual(zero_matrix(matrix), expeted)

if __name__ == '__main__':
    unittest.main()
