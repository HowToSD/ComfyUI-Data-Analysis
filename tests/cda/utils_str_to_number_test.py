import os
import sys
import unittest

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from cda.utils import str_to_number

class TestUtils(unittest.TestCase):
    def test_str_to_number(self):
        # Test integer conversion
        self.assertEqual(str_to_number("42"), 42)
        
        # Test float conversion
        self.assertEqual(str_to_number("3.14"), 3.14)
        
        # Test negative integer
        self.assertEqual(str_to_number("-10"), -10)

        # Test negative float
        self.assertEqual(str_to_number("-2.71"), -2.71)

        # Test zero
        self.assertEqual(str_to_number("0"), 0)
        self.assertEqual(str_to_number("0.0"), 0.0)

        # Test invalid input (empty string)
        with self.assertRaises(ValueError):
            str_to_number("")

        # Test invalid input (non-numeric string)
        with self.assertRaises(ValueError):
            str_to_number("abc")

if __name__ == "__main__":
    unittest.main()

