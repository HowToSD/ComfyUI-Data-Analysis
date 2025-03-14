import os
import sys
import unittest
import pandas as pd
import ast
from typing import Any, Dict

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pandas_wrapper.pandas_replace_advanced import PandasReplaceAdvanced


class TestPandasReplaceAdvanced(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.node = PandasReplaceAdvanced()
        cls.df = pd.DataFrame(
            {
                "col1": ["cat", "dog", "fish"],
                "col2": ["mountain", "ocean", "forest"],
            }
        )

    def test_valid_replacement(self):
        test_cases = [
            ('{"cat": 1, "dog": 2.34}', {"col1": [1, 2.34, "fish"], "col2": ["mountain", "ocean", "forest"]}),
            ('{"mountain": "hill", "forest": "jungle"}', {"col1": ["cat", "dog", "fish"], "col2": ["hill", "ocean", "jungle"]}),
        ]
        for replacements, expected_data in test_cases:
            with self.subTest(replacements=replacements):
                result_df = self.node.f(self.df, replacements)[0]
                expected_df = pd.DataFrame(expected_data)
                pd.testing.assert_frame_equal(result_df, expected_df)

    def test_invalid_replacement_value_error(self):
        invalid_cases = [
            '["cat", "lion"]',  # List is not allowed
            '{"cat": ["lion", "tiger"]}',  # List is not allowed
            '{"dog": {"wolf": "coyote"}}'  # Nested dict is not allowed
        ]
        for invalid_pairs in invalid_cases:
            with self.subTest(invalid_pairs=invalid_pairs):
                with self.assertRaises(ValueError):
                    self.node.f(self.df, invalid_pairs)

    def test_invalid_replacement_syntax_error(self):
        invalid_cases = [
            '{"mountain": ()"hill", "ocean")}',  # Syntax error
        ]
        for invalid_pairs in invalid_cases:
            with self.subTest(invalid_pairs=invalid_pairs):
                with self.assertRaises(SyntaxError):
                    self.node.f(self.df, invalid_pairs)



if __name__ == "__main__":
    unittest.main()
