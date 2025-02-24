import os
import sys
import unittest
import json
import numpy as np
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
print(MODULE_ROOT)

from pandas_wrapper.utils import index_to_jsons, jsons_to_index

class TestIndexJsonConversion(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.index_int = pd.Index([1, 2, 3], name="test_index_int")
        self.index_float = pd.Index([1.1, 2.2, 3.3], name="test_index_float")
        self.index_str = pd.Index(["a", "b", "c"], name="test_index_str")
        self.index_mixed = pd.Index([1, "text", 3.5], name="test_index_mixed")
        self.index_no_name = pd.Index([1, "text", 3.5])

    def test_index_to_jsons_and_back(self):
        """Test conversion from Index to JSON and back"""
        for index in [self.index_int, self.index_float, self.index_str, self.index_mixed]:
            with self.subTest(index=index):
                json_str = index_to_jsons(index)
                reconstructed_index = jsons_to_index(json_str)
                self.assertTrue(index.equals(reconstructed_index), f"Failed for index: {index.name}")

    def test_json_format(self):
        """Test if JSON output is correctly formatted"""
        json_str = index_to_jsons(self.index_int)
        data = json.loads(json_str)

        self.assertIn("index", data)
        self.assertIn("name", data)
        self.assertEqual(data["name"], "test_index_int")

    def test_json_format_no_name(self):
        """Test if JSON output is correctly formatted"""
        json_str = index_to_jsons(self.index_no_name)
        data = json.loads(json_str)

        self.assertIn("index", data)
        self.assertIn("name", data)
        self.assertTrue(data["name"] is None)


if __name__ == "__main__":
    unittest.main()
