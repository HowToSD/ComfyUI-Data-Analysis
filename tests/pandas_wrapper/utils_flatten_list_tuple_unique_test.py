import os
import sys
import unittest
from typing import Any, List, Tuple, Union, Set

PROJECT_ROOT = os.path.realpath(os.path.join(__file__, "..", "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pandas_wrapper.utils import flatten_list_tuple_unique


class TestFlattenListTupleUnique(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (["a", "b", "c"], {"a", "b", "c"}),  # Strings only
            ([1, 2, 3], {1, 2, 3}),  # Integers only
            (["a", 1], {"a", 1}),  # Mixed types
            (["a", ("b", "c", "d"), (1, 2, 3), ("b", "c", "e")], {"a", "b", "c", "d", 1, 2, 3, "e"}),  # Nested tuples
            ([("x", "y"), ["y", "z"]], {"x", "y", "z"}),  # Nested lists and tuples
            ([1, (2, [3, (4, 5)]), 6, (7, [8, 9])], {1, 2, 3, 4, 5, 6, 7, 8, 9}),  # Deep nesting
            ([], set()),  # Empty list
            ([()], set()),  # Empty tuple inside a list
            ([None, [None, None]], {None}),  # None values
            ([True, False, 1, 0], {True, False}),  # Boolean values (Python treats True as 1 and False as 0)
        ]

    def test_flatten_list_tuple_unique(self):
        for input_data, expected_output in self.test_cases:
            with self.subTest(input_data=input_data):
                self.assertEqual(flatten_list_tuple_unique(input_data), expected_output)


if __name__ == "__main__":
    unittest.main()

