import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_pow import PtPow


class TestPtPow(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtPow()

        # Test cases: (Tensor A, Tensor B, Expected result)
        self.test_cases = [
            (torch.tensor([2.0, 3.0, 4.0]), torch.tensor([3.0, 2.0, 1.0]), torch.tensor([8.0, 9.0, 4.0])),  # 2^3, 3^2, 4^1
            (torch.ones(3, 3) * 4, torch.ones(3, 3) * 2, torch.ones(3, 3) * 16),  # 4^2 = 16
            (torch.full((2, 2), 5.0), torch.full((2, 2), 3.0), torch.full((2, 2), 125.0)),  # 5^3 = 125
            (torch.tensor([[2.0], [3.0]]), torch.tensor([[4.0], [5.0]]), torch.tensor([[16.0], [243.0]])),  # 2^4 = 16, 3^5 = 243
        ]

    def test_power(self):
        """Test tensor exponentiation."""
        for tens_a, tens_b, expected in self.test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                result, = self.node.f(tens_a, tens_b)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected power computation
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
