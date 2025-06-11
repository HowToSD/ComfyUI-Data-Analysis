import os
import sys
import unittest

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from cda.py_list_to_string import PyListToString

class TestPyListToString(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PyListToString()
        self.test_cases = [
            ([1,2,3], "[1, 2, 3]"),
            (["apple", "banana"], "['apple', 'banana']"),
            ([], "[]")
        ]

    def test_list_to_string(self):
        """Test converting a list to string."""
        for value, expected in self.test_cases:
            with self.subTest(value=value):
                retval = self.node.f(value=value)[0]
                self.assertEqual(retval, expected, f"Mismatch for value={value}")


if __name__ == "__main__":
    unittest.main()