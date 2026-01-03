import numpy as np
import scipy.linalg

class LUSolver:
    """
    Handles LU Decomposition and solving linear systems Ax=b.
    """
    
    @staticmethod
    def solve_system(A_list, b_list):
        """
        Solves Ax=b using LU decomposition.
        
        Args:
            A_list (list of lists): The coefficient matrix A.
            b_list (list): The dependent variable vector b.
            
        Returns:
            dict: Contains 'L', 'U', 'x' (solution), 'det' (determinant), and 'stable' (boolean).
        """
        try:
            A = np.array(A_list, dtype=float)
            b = np.array(b_list, dtype=float)
            
            # Check for square matrix
            if A.shape[0] != A.shape[1]:
                raise ValueError("Matrix A must be square.")
                
            # LU Decomposition
            # scipy.linalg.lu returns P, L, U such that A = P @ L @ U
            P, L, U = scipy.linalg.lu(A)
            
            # Calculate Determinant via U (product of diagonal elements)
            # Since det(A) = det(P) * det(L) * det(U)
            # det(L) is usually 1 (unit lower triangular)
            # det(P) is +/- 1
            # We focus on U for singularity check in this context as requested
            det_U = np.prod(np.diag(U))
            
            # Full determinant (including P and L sign flip)
            det_A = scipy.linalg.det(A)
            
            is_stable = not np.isclose(det_A, 0.0)
            
            x = None
            if is_stable:
                x = scipy.linalg.solve(A, b)
            
            return {
                'L': L.tolist(),
                'U': U.tolist(),
                'x': x.tolist() if x is not None else None,
                'det': det_A,
                'stable': is_stable,
                'error': None
            }
            
        except np.linalg.LinAlgError as e:
            return {
                'L': None, 'U': None, 'x': None, 'det': 0.0, 'stable': False, 'error': str(e)
            }
        except Exception as e:
            return {
                'L': None, 'U': None, 'x': None, 'det': None, 'stable': False, 'error': str(e)
            }
