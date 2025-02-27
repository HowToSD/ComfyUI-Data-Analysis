import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_abs import PtAbs  # Updated import to PtAbs


class TestPtAbs(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtAbs()

        # Test cases: (Tensor A, Expected result)
        self.test_cases = [
            (torch.tensor([-1, 2, -3, 4], dtype=torch.float32), torch.tensor([1, 2, 3, 4], dtype=torch.float32)),  # Mixed positive/negative
            (torch.tensor([0, -5, 10, -15], dtype=torch.int32), torch.tensor([0, 5, 10, 15], dtype=torch.int32)),  # Integer case
            (torch.tensor([[-1.5, 2.3], [-3.7, 4.9]], dtype=torch.float32), torch.tensor([[1.5, 2.3], [3.7, 4.9]], dtype=torch.float32)),  # 2D case
            (torch.tensor([[-100, 0, 50], [-25, -75, 100]], dtype=torch.int64), torch.tensor([[100, 0, 50], [25, 75, 100]], dtype=torch.int64)),  # Large numbers
            (torch.full((2, 2), -7.7, dtype=torch.float32), torch.full((2, 2), 7.7, dtype=torch.float32)),  # Constant matrix
        ]

    def test_absolute_value(self):
        """Test tensor element-wise absolute value using torch.abs()."""
        for tens_a, expected in self.test_cases:
            with self.subTest(tens_a=tens_a):
                result, = self.node.f(tens_a)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected absolute value operation
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
