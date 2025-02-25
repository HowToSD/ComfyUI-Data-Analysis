import os
import sys
import unittest
import numpy as np
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_to_numpy import PandasToNumpy

class TestPandasToNumpy(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasToNumpy()
        
        self.test_cases = [
            # Rank 1
            (pd.DataFrame([1, 2, 3]), np.array([[1], [2], [3]])),
            (pd.DataFrame([1.1, 2.2, 3.3]), np.array([[1.1], [2.2], [3.3]])),
            (pd.DataFrame(["a", "b", "c"]), np.array([["a"], ["b"], ["c"]], dtype=object)),
            (pd.DataFrame([True, False, True]), np.array([[True], [False], [True]])),

            # Rank 2
            (pd.DataFrame([[1, 2], [3, 4]]), np.array([[1, 2], [3, 4]])),
            (pd.DataFrame([[1.1, 2.2], [3.3, 4.4]]), np.array([[1.1, 2.2], [3.3, 4.4]])),
            (pd.DataFrame([["a", "b"], ["c", "d"]]), np.array([["a", "b"], ["c", "d"]], dtype=object)),
            (pd.DataFrame([[True, False], [False, True]]), np.array([[True, False], [False, True]])),

            # Invalid cases
            (None, TypeError),
            ("not a DataFrame", TypeError),
            (np.array([[1, 2], [3, 4]]), TypeError)
        ]

    def test_dataframe_to_numpy(self):
        """Test NumPy array conversion from various Pandas DataFrames."""
        for dataframe, expected in self.test_cases:
            with self.subTest(dataframe=dataframe):
                if isinstance(expected, type) and issubclass(expected, Exception):
                    with self.assertRaises(expected):
                        self.node.f(dataframe)
                else:
                    retval = self.node.f(dataframe)[0]

                    # Ensure the return type is a NumPy array
                    self.assertTrue(isinstance(retval, np.ndarray))

                    # Check array equality
                    np.testing.assert_array_equal(retval, expected)

if __name__ == "__main__":
    unittest.main()
