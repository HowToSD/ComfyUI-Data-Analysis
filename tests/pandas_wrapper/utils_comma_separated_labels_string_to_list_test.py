import os
import sys
import unittest
from typing import List

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pandas_wrapper.utils import comma_separated_labels_string_to_list

class TestCommaSeparatedLabelsStringToList(unittest.TestCase):
    """
    Unit tests for `comma_separated_labels_string_to_list` function.
    """
    
    def setUp(self) -> None:
        """
        Sets up the test environment before each test case.
        """
        pass

    def test_valid_column_strings(self) -> None:
        """
        Tests `comma_separated_labels_string_to_list` with various valid input strings.
        """
        self.assertEqual(comma_separated_labels_string_to_list("label1,label2,label3"), ["label1", "label2", "label3"])
        self.assertEqual(comma_separated_labels_string_to_list("  label1  , label2 ,label3  "), ["label1", "label2", "label3"])
        self.assertEqual(comma_separated_labels_string_to_list("a,b,c,d"), ["a", "b", "c", "d"])
        self.assertEqual(comma_separated_labels_string_to_list("one"), ["one"])
        self.assertEqual(comma_separated_labels_string_to_list(""), [])
        self.assertEqual(comma_separated_labels_string_to_list(None), [])
        self.assertEqual(comma_separated_labels_string_to_list(" , , , "), ["", "", "", ""])

if __name__ == "__main__":
    unittest.main()


