import os
import sys
import unittest
from datetime import datetime

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from cda.py_string_to_datetime import PyStringToDatetime

class TestPyStringToDatetime(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PyStringToDatetime()
        self.test_cases = [
            ("2023-03-15 12:00:00", "%Y-%m-%d %H:%M:%S", datetime(2023, 3, 15, 12, 0, 0)),
            ("2024-06-01 09:30:00", "%Y-%m-%d %H:%M:%S", datetime(2024, 6, 1, 9, 30, 0)),
            ("15/03/2023 12:00", "%d/%m/%Y %H:%M", datetime(2023, 3, 15, 12, 0)),
            ("01-06-2024", "%d-%m-%Y", datetime(2024, 6, 1))
        ]

    def test_string_to_datetime(self):
        """Test converting a string to datetime."""
        for value, date_format, expected in self.test_cases:
            with self.subTest(value=value, date_format=date_format):
                retval = self.node.f(value=value, date_format=date_format)[0]
                self.assertEqual(retval, expected, f"Mismatch for value={value} with format={date_format}")

if __name__ == "__main__":
    unittest.main()