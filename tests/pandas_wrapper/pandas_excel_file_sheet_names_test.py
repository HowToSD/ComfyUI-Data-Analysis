import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_excel_file_sheet_names import PandasExcelFileSheetNames


class TestPandasExcelFileSheetNames(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasExcelFileSheetNames()
        self.test_file_path = os.path.join(
                                os.path.dirname(__file__), "..", "..",
                                "examples", "datasets", "test_file.xlsx")
        
        self.test_data_list = [
                "Sheet1",
                "FruitPrice"
        ]

    def test_excel_file_sheet_names(self):
        """Reads sheet names from an excel file.
        """
        expected = self.test_data_list
        actual = self.node.f(self.test_file_path)[0]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
