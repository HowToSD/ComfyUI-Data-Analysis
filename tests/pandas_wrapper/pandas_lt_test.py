import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_lt import PandasLt

class TestPandasLt(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasLt()
        self.test_cases = [
            # Test where all values are True
            (
                pd.DataFrame({"a": [1.5, 2.5]}, index=["row1", "row2"]),
                pd.DataFrame({"a": [2.0, 3.0]}, index=["row1", "row2"]),
                pd.DataFrame({"a": [True, True]}, index=["row1", "row2"])
            ),
            # Test with integer (still True)
            (
                pd.DataFrame({"a": [3, 40]}, index=[0, 1]),
                pd.DataFrame({"a": [4, 50]}, index=[0, 1]),
                pd.DataFrame({"a": [True, True]}, index=[0, 1])
            ),
            # Test with integer column labels
            (
                pd.DataFrame({1: [10.0, 20.0]}, index=[0, 1]),
                pd.DataFrame({1: [15.0, 20.0]}, index=[0, 1]),
                pd.DataFrame({1: [True, False]}, index=[0, 1])
            ),
            # Test with a False case (a >= b)
            (
                pd.DataFrame({"a": [7.0]}, index=["row1"]),
                pd.DataFrame({"a": [7.0]}, index=["row1"]),
                pd.DataFrame({"a": [False]}, index=["row1"])
            ),
            # Another False case with an integer column label
            (
                pd.DataFrame({2: [9.5]}, index=["row1"]),
                pd.DataFrame({2: [8.0]}, index=["row1"]),
                pd.DataFrame({2: [False]}, index=["row1"])
            ),
        ]

    def test_lt_operation(self):
        """Test less-than operation between two pandas DataFrames."""
        for df_a, df_b, expected in self.test_cases:
            with self.subTest(df_a=df_a, df_b=df_b):
                retval = self.node.f(df_a, df_b)
                self.assertIsInstance(retval, tuple, "Return value should be a tuple.")
                self.assertEqual(len(retval), 1, "Return tuple should have a single DataFrame.")
                pd.testing.assert_frame_equal(retval[0], expected)

if __name__ == "__main__":
    unittest.main()
