import os
import sys
import unittest
import numpy as np


PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from numpy_wrapper.numpy_float_create import NumpyFloatCreate

class TestNumpyFloatCreate(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = NumpyFloatCreate()

        # Test cases covering rank 0 (scalar) to rank 5 tensors
        self.test_cases = [
            # Rank 0 (scalar)
            ("12345", np.array(12345, dtype=np.float32)),
            ("12345.6", np.array(12345.6, dtype=np.float32)),

            # Rank 1 (1D array)
            ("[1, 2, 3]", np.array([1, 2, 3], dtype=np.float32)),
            ("[1.1, 2.2, 3.3]", np.array([1.1, 2.2, 3.3], dtype=np.float32)),

            # Rank 2 (2D matrix)
            ("[[1, 2, 3], [4, 5, 6]]", np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)),
            ("[[1.1, 2.2], [3.3, 4.4]]", np.array([[1.1, 2.2], [3.3, 4.4]], dtype=np.float32)),

            # Rank 3 (3D tensor)
            ("[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]", 
             np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=np.float32)),
            
            # Rank 4 (4D tensor)
            ("[[[[1, 2], [3, 4]]], [[[5, 6], [7, 8]]]]", 
             np.array([[[[1, 2], [3, 4]]], [[[5, 6], [7, 8]]]], dtype=np.float32)),

            # Rank 5 (5D tensor)
            ("[[[[[1], [2]], [[3], [4]]]], [[[[5], [6]], [[7], [8]]]]]", 
             np.array([[[[[1], [2]], [[3], [4]]]], [[[[5], [6]], [[7], [8]]]]], dtype=np.float32)),
        ]

    def test_create_ndarray(self):
        """Test NumPy ndarray creation from various structured inputs."""
        for data_str, expected_array in self.test_cases:
            with self.subTest(data=data_str):
                retval = self.node.f(data_str)[0]

                # Ensure the returned value is a NumPy array
                self.assertTrue(isinstance(retval, np.ndarray), f"Expected ndarray, got {type(retval)}")

                # Ensure the dtype is float32
                self.assertEqual(retval.dtype, np.float32, f"Dtype mismatch for input: {data_str}")

                # Ensure the shape matches
                self.assertEqual(retval.shape, expected_array.shape, 
                                 f"Shape mismatch for input: {data_str} (Expected {expected_array.shape}, got {retval.shape})")

                # Ensure values match
                np.testing.assert_array_equal(retval, expected_array, 
                                              f"Value mismatch for input: {data_str}")

if __name__ == "__main__":
    unittest.main()
