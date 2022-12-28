import pytest
from rotate_matrix import rotate

def test_simple_example():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    expeted = True
    assert rotate(matrix) == expeted