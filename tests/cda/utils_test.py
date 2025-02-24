import os
import sys
import unittest

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from cda.utils import python_dict_first_value_len

class TestUtils(unittest.TestCase):
    def test_python_dict_first_value_len(self):
        """Test python_dict_first_value_len with various input cases."""
        
        test_cases = [
            ({"a": [1, 2, 3]}, 3, "List case"),
            ({"a": {"x": 1, "y": 2}}, 2, "Dict case"),
            ({"a": 42}, 1, "Integer case"),
            ({"a": 3.14}, 1, "Float case"),
            ({"a": "hello"}, 1, "String case"),
            ({"a": True}, 1, "Boolean case"),
            ({"a": None}, 1, "None as value case"),
            ({"a": [], "b": "extra"}, 0, "Empty list case"),
            ({"a": {}}, 0, "Empty dict case"),
        ]

        for data, expected, desc in test_cases:
            with self.subTest(msg=desc, data=data):
                self.assertEqual(python_dict_first_value_len(data), expected)

        # Test ValueError for None input
        with self.assertRaises(ValueError, msg="None input case"):
            python_dict_first_value_len(None)

        # Test ValueError for empty dictionary
        with self.assertRaises(ValueError, msg="Empty dictionary case"):
            python_dict_first_value_len({})

if __name__ == "__main__":
    unittest.main()
