import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from seaborn_wrapper.sns_line_pt import SNSLinePt

class TestSNSLinePt(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = SNSLinePt()
        self.test_cases = [
            (
                torch.stack(
                    [
                        torch.arange(1, 10, dtype=torch.int64),
                        torch.arange(1, 10, dtype=torch.int64)*2
                    ],
                    dim=1
                ),
                "1", "y"
            ),
            (
                torch.stack(
                    [
                        torch.arange(1, 10, dtype=torch.int64),
                        torch.arange(1, 10, dtype=torch.int64)*2,
                        torch.arange(1, 10, dtype=torch.int64)*3
                    ],
                    dim=1
                ),
                "1,2", "profit,sales"
            )
        ]

    def test_1(self):
        """
        Tests plot.
        """
        for tens, y_axis_dims, labels in self.test_cases:
            with self.subTest(data=y_axis_dims):
                
                self.node.f(
                    tens=tens,
                    x_axis_dim = 0,
                    y_axis_dims = y_axis_dims,
                    title="test",
                    x_axis_label = "x",
                    y_axis_label = "y",
                    legend_label=labels,
                    x_tick_as_int=True)


if __name__ == "__main__":
    unittest.main()
