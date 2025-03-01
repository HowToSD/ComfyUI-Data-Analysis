import os
import sys
import unittest

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from cda.utils import str_to_number_with_default

class TestUtils(unittest.TestCase):
    def test_str_to_number_with_default(self):
        # Test integer conversion
        self.assertEqual(str_to_number_with_default("42", 0), 42)
        
        # Test float conversion
        self.assertEqual(str_to_number_with_default("3.14", 0.0), 3.14)
        
        # Test negative integer
        self.assertEqual(str_to_number_with_default("-10", 0), -10)

        # Test negative float
        self.assertEqual(str_to_number_with_default("-2.71", 0.0), -2.71)

        # Test zero
        self.assertEqual(str_to_number_with_default("0", 1), 0)
        self.assertEqual(str_to_number_with_default("0.0", 1.0), 0.0)

        # Test empty string returning default value
        self.assertEqual(str_to_number_with_default("", 42), 42)
        self.assertEqual(str_to_number_with_default("", -3.5), -3.5)

if __name__ == "__main__":
    unittest.main()
