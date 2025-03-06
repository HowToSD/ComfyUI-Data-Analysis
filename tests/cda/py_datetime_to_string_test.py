import os
import sys
import unittest
from datetime import datetime

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from cda.py_datetime_to_string import PyDatetimeToString

class TestPyDatetimeToString(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PyDatetimeToString()
        self.test_cases = [
            (datetime(2023, 3, 15, 12, 0, 0), "%Y-%m-%d %H:%M:%S", "2023-03-15 12:00:00"),
            (datetime(2024, 6, 1, 9, 30, 0), "%Y-%m-%d %H:%M:%S", "2024-06-01 09:30:00"),
            (datetime(2023, 3, 15, 12, 0), "%d/%m/%Y %H:%M", "15/03/2023 12:00"),
            (datetime(2024, 6, 1), "%d-%m-%Y", "01-06-2024")
        ]

    def test_datetime_to_string(self):
        """Test converting a datetime to string."""
        for value, date_format, expected in self.test_cases:
            with self.subTest(value=value, date_format=date_format):
                retval = self.node.f(value=value, date_format=date_format)[0]
                self.assertEqual(retval, expected, f"Mismatch for value={value} with format={date_format}")

if __name__ == "__main__":
    unittest.main()
