import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_load_excel import PandasLoadExcel


class TestPandasLoadExcel(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasLoadExcel()
        self.test_file_path = os.path.join(
                                os.path.dirname(__file__), "..", "..",
                                "examples", "datasets", "test_file.xlsx")
        
        self.test_data_list = [
            (
                "Sheet1",
                pd.DataFrame(
                    {
                        "Item": ["Bat", "Racquet", "Glove", "Hockey stick", "Soccer ball"],
                        "Qty": [3, 4, 5, 6, 7]
                    },
                    index = [0, 1, 2, 3, 4]
                ),
            ),
            (
                "FruitPrice",
                pd.DataFrame(
                    {
                        "Fruit": ["Apple", "Banana", "Coconut", "Donut"],
                        "Price": [1.23, 2.34, 3.45, 4.56]
                    },
                    index = [0, 1, 2, 3]
                )
            ),
            (
                "",  # Leaving the sheet name blank should read the first sheet.
                pd.DataFrame(
                    {
                        "Item": ["Bat", "Racquet", "Glove", "Hockey stick", "Soccer ball"],
                        "Qty": [3, 4, 5, 6, 7]
                    },
                    index = [0, 1, 2, 3, 4]
                ),
            ),
        ]
    def test_read_excel(self):
        """Reads multiple sheets from an excel file.
        """
        for test_data in self.test_data_list:
            with self.subTest(test_data=test_data):
                sheet_name = test_data[0]
                expected = test_data[1]
                df = self.node.f(self.test_file_path, sheet_name=sheet_name)[0]
                pd.testing.assert_frame_equal(df, expected)


if __name__ == "__main__":
    unittest.main()
