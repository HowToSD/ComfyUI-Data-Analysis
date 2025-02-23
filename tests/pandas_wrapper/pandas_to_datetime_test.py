import os
import sys
import unittest
import pandas as pd
import pandas.api.types as ptypes

PROJECT_ROOT = os.path.realpath(os.path.join(__file__, "..", "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
print(MODULE_ROOT)

from pandas_wrapper.pandas_to_datetime import PandasToDatetime

class Test(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.node = PandasToDatetime()
        self.pd_date = pd.DataFrame({
            "A": ["2015-01-23", "2013-06-30"],
            "B": ["2005-02-24", "2015-09-06"],
            "C": [123.45, 987.65],
        })

        self.pd_date_time = pd.DataFrame({
            "A": ["2015-01-23 00:12:34", "2013-06-30 12:50:59"],
            "B": [123.45, 987.65],
        })

        self.pd_time = pd.DataFrame({
            "A": ["00:12:34", "12:50:59"],
            "B": [123.45, 987.65],
        })

    def test_date(self):
        """Test"""
        df2 = self.node.f(self.pd_date, column_names="A,B", date_format="%Y-%m-%d")[0]
        self.assertEqual(df2.at[0, "A"], pd.Timestamp("2015-01-23"))
        self.assertEqual(df2.at[0, "C"], 123.45)

    def test_date_time(self):
        """Test"""
        df3 = self.node.f(self.pd_date_time, column_names="A", date_format="%Y-%m-%d %H:%M:%S")[0]
        self.assertTrue(ptypes.is_datetime64_any_dtype(df3["A"]))
        self.assertTrue(ptypes.is_float_dtype(df3["B"]))
        self.assertEqual(df3.at[0, "A"], pd.Timestamp("2015-01-23 00:12:34"))
        self.assertEqual(df3.at[0, "B"], 123.45)

    def test_time(self):
        """Test"""
        df3 = self.node.f(self.pd_time, column_names="A", date_format="%H:%M:%S")[0]
        self.assertTrue(ptypes.is_datetime64_any_dtype(df3["A"]))
        self.assertEqual(df3.at[0, "A"], pd.Timestamp("1900-01-01 00:12:34"))
        self.assertEqual(df3.at[0, "B"], 123.45)


if __name__ == "__main__":
    unittest.main()
