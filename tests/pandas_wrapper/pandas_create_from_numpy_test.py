import os
import sys
import unittest
import numpy as np
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_create_from_numpy import PandasCreateFromNumpy

class TestPandasCreateFromNumpy(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasCreateFromNumpy()
        
        self.test_cases = [
            # Rank 0
            (np.array(42), ValueError),
            (np.array(3.14), ValueError),
            (np.array("hello"), ValueError),
            (np.array(True), ValueError),
            
            # Rank 1
            (np.array([1, 2, 3]), pd.DataFrame([1, 2, 3])),
            (np.array([1.1, 2.2, 3.3]), pd.DataFrame([1.1, 2.2, 3.3])),
            (np.array(["a", "b", "c"]), pd.DataFrame(["a", "b", "c"])),
            (np.array([True, False, True]), pd.DataFrame([True, False, True])),
            
            # Rank 2
            (np.array([[1, 2], [3, 4]]), pd.DataFrame([[1, 2], [3, 4]])),
            (np.array([[1.1, 2.2], [3.3, 4.4]]), pd.DataFrame([[1.1, 2.2], [3.3, 4.4]])),
            (np.array([["a", "b"], ["c", "d"]]), pd.DataFrame([["a", "b"], ["c", "d"]])),
            (np.array([[True, False], [False, True]]), pd.DataFrame([[True, False], [False, True]])),
            
            # Rank 3 (Invalid)
            (np.array([[[1, 2], [3, 4]]]), ValueError),
            (np.array([[["x", "y"], ["z", "w"]]]), ValueError),
            
            # Rank 4 (Invalid)
            (np.random.rand(2, 2, 2, 2), ValueError)
        ]
    
    def test_create_dataframe(self):
        """Test DataFrame creation from various NumPy arrays."""
        for data, expected in self.test_cases:
            with self.subTest(data=data):
                if isinstance(expected, type) and issubclass(expected, Exception):
                    with self.assertRaises(expected):
                        self.node.f(data)
                else:
                    retval = self.node.f(data)[0]
                    
                    # Test if DataFrame structure matches
                    self.assertTrue(isinstance(retval, pd.DataFrame))
                    
                    # Test if data matches
                    pd.testing.assert_frame_equal(retval, expected)

if __name__ == "__main__":
    unittest.main()
