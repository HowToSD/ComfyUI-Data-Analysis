import os
import sys
import unittest
import numpy as np


PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from numpy_wrapper.numpy_squeeze import NumpySqueeze  # Importing the NumpySqueeze class


class TestNumpySqueeze(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = NumpySqueeze()

        # Define test cases: (input_array, dim, expected_shape)
        self.test_cases = [
            # Case 1: Squeezing a singleton dimension
            (np.ones((1, 3, 4)), 0, (3, 4)),  # (1,3,4) -> (3,4)
            (np.ones((2, 1, 4)), 1, (2, 4)),
            (np.ones((100, 1)), 1, (100, )),

            # Case 2: Multiple singleton dimensions, squeezing one
            (np.ones((1, 2, 1, 4)), 2, (1, 2, 4)),

            # Case 3: Squeezing a negative index
            (np.ones((2, 3, 1)), -1, (2, 3)),

            # Case 4: Squeezing all size 1 dimensions
            (np.ones((1, 1, 1)), 0, (1, 1)),
            (np.ones((1, 1, 1)), 1, (1, 1)),
            (np.ones((1, 1, 1)), 2, (1, 1)),

            # Case 5: Squeezing a 1d array with a single element to a scalar
            (np.ones((1,)), 0, ()),
        ]

    def test_squeeze(self):
        """Test array squeeze operation on various dimensions."""
        for input_array, dim, expected_shape in self.test_cases:
            with self.subTest(input_shape=input_array.shape, dim=dim):
                result, = self.node.f(input_array, dim)

                # Ensure return value is a array
                self.assertTrue(isinstance(result, np.ndarray), "Output is not a array")

                # Ensure result has correct shape
                self.assertEqual(result.shape, expected_shape, f"Expected shape {expected_shape}, got {result.shape}")

                # Ensure result has the same dtype
                self.assertEqual(result.dtype, input_array.dtype, "Dtype mismatch after squeeze operation")


if __name__ == "__main__":
    unittest.main()
