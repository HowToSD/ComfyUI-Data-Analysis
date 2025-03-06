import os
import sys
import unittest

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from cda.py_string_to_int import PyStringToInt

class TestPyStringToInt(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PyStringToInt()
        self.test_cases = [
            ("3", 3),
            ("27", 27),
            ("100", 100),
            ("-42", -42)
        ]

    def test_string_to_int(self):
        """Test converting a string to int."""
        for value, expected in self.test_cases:
            with self.subTest(value=value):
                retval = self.node.f(value=value)[0]
                self.assertEqual(retval, expected, f"Mismatch for value={value}")

if __name__ == "__main__":
    unittest.main()
