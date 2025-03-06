import os
import sys
import unittest

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from cda.py_float_to_string import PyFloatToString

class TestPyFloatToString(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PyFloatToString()
        self.test_cases = [
            (3.14, "3.14"),
            (2.71, "2.71"),
            (0.577, "0.577"),
            (1.618, "1.618")
        ]

    def test_float_to_string(self):
        """Test converting a float to string."""
        for value, expected in self.test_cases:
            with self.subTest(value=value):
                retval = self.node.f(value=value)[0]
                self.assertEqual(retval, expected, f"Mismatch for value={value}")

if __name__ == "__main__":
    unittest.main()