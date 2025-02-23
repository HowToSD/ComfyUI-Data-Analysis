import os
import sys
import unittest
import json
import numpy as np
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(__file__, "..", "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
print(MODULE_ROOT)
from pandas_wrapper.utils import series_to_jsons
from pandas_wrapper.utils import jsons_to_series

class TestSeriesJsonConversion(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.series_int = pd.Series([10, 20, 30], index=["a", "b", "c"], name="test_series_int")
        self.series_np_int64 = pd.Series(np.array([10, 20, 30], dtype=np.int64),
                                         index=["a", "b", "c"],
                                         name="test_series_np_int64")
        self.series_np_int64_2 = pd.Series(np.array([10, 20, 30], dtype=np.int64),
                                           index=np.array([1, 2, 3], dtype=np.int64),
                                           name="test_series_np_int64_2")
        self.series_float = pd.Series([1.1, 2.2, 3.3], index=["x", "y", "z"], name="test_series_float")
        self.series_str = pd.Series(["apple", "banana", "cherry"], index=[0, 1, 2], name="test_series_str")
        self.series_mixed = pd.Series([1, "text", 3.5], index=["one", "two", "three"], name="test_series_mixed")

    def test_series_to_jsons_and_back(self):
        """Test conversion from Series to JSON and back"""
        for series in [self.series_int, self.series_np_int64, self.series_np_int64_2,
                       self.series_float, self.series_str, self.series_mixed]:
            with self.subTest(series=series):
                json_str = series_to_jsons(series)
                reconstructed_series = jsons_to_series(json_str)
                self.assertTrue(series.equals(reconstructed_series), f"Failed for series: {series.name}")

    def test_json_format(self):
        """Test if JSON output is correctly formatted"""
        json_str = series_to_jsons(self.series_int)
        data = json.loads(json_str)
        
        self.assertIn("array", data)
        self.assertIn("index", data)
        self.assertIn("name", data)
        self.assertEqual(data["name"], "test_series_int")

if __name__ == "__main__":
    unittest.main()
