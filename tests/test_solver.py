import unittest
import numpy as np
from core.solver import LUSolver

class TestLUSolver(unittest.TestCase):
    def test_solve_stable_system(self):
        # A = [[3, 1], [1, 2]], b = [9, 8]
        # Solution: x = [2, 3]
        A = [[3, 1], [1, 2]]
        b = [9, 8]
        result = LUSolver.solve_system(A, b)
        
        self.assertTrue(result['stable'])
        self.assertIsNotNone(result['x'])
        np.testing.assert_array_almost_equal(result['x'], [2, 3])
        self.assertAlmostEqual(result['det'], 5.0)

    def test_singular_matrix(self):
        # A = [[1, 1], [1, 1]] -> det = 0
        A = [[1, 1], [1, 1]]
        b = [2, 2]
        result = LUSolver.solve_system(A, b)
        
        self.assertFalse(result['stable'])
        self.assertIsNone(result['x'])
        self.assertAlmostEqual(result['det'], 0.0)

    def test_invalid_input(self):
        # Non-square matrix
        A = [[1, 2, 3], [4, 5, 6]]
        b = [1, 2]
        result = LUSolver.solve_system(A, b)
        
        self.assertFalse(result['stable'])
        self.assertIsNotNone(result['error'])

if __name__ == '__main__':
    unittest.main()
