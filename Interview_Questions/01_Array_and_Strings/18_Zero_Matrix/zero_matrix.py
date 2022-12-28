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
    
