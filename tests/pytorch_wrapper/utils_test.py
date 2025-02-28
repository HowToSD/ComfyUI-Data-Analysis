import os
import sys
import unittest

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.utils import str_to_dim


class TestStrToDim(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        pass

    def test_valid_integer(self):
        """Test parsing a valid integer string."""
        self.assertEqual(str_to_dim("5"), 5)

    def test_valid_tuple(self):
        """Test parsing a valid tuple string."""
        self.assertEqual(str_to_dim("(1, 2, 3)"), (1, 2, 3))

    def test_valid_list(self):
        """Test parsing a valid list string (should be converted to tuple)."""
        self.assertEqual(str_to_dim("[4, 5, 6]"), (4, 5, 6))

    def test_empty_string(self):
        """Test empty string input should return None."""
        self.assertIsNone(str_to_dim(""))

    def test_invalid_string(self):
        """Test invalid string input should raise ValueError."""
        with self.assertRaises(ValueError):
            str_to_dim("invalid")

    def test_mixed_type_list(self):
        """Test a list with mixed types should raise ValueError."""
        with self.assertRaises(ValueError):
            str_to_dim("[1, 'a', 3]")

    def test_nested_tuple(self):
        """Test a nested tuple should raise ValueError."""
        with self.assertRaises(ValueError):
            str_to_dim("((1, 2), 3)")

    def test_dict_input(self):
        """Test a dictionary input should raise ValueError."""
        with self.assertRaises(ValueError):
            str_to_dim("{'a': 1, 'b': 2}")

if __name__ == "__main__":
    unittest.main()
