import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_arange import PtArange


class TestPtArange(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtArange()

        # Test cases: (start, end, step, dtype, expected_tensor, expected_dtype)
        self.test_cases = [
            ("0", "5", "1", "int32", torch.tensor([0, 1, 2, 3, 4], dtype=torch.int32), torch.int32),  # Simple range
            ("-3", "3", "1", "float32", torch.tensor([-3, -2, -1, 0, 1, 2], dtype=torch.float32), torch.float32),  # Negative start
            ("1.5", "4.5", "1", "float64", torch.tensor([1.5, 2.5, 3.5], dtype=torch.float64), torch.float64),  # Floating point step
            ("10", "0", "-2", "int64", torch.tensor([10, 8, 6, 4, 2], dtype=torch.int64), torch.int64),  # Decreasing range
            ("", "5", "1", "int8", torch.tensor([0, 1, 2, 3, 4], dtype=torch.int8), torch.int8),  # Default start (0)
            ("0", "10", "", "uint8", torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=torch.uint8), torch.uint8),  # Default step (1)
        ]

    def test_arange_tensor_creation(self):
        """Test tensor generation using torch.arange(), including values and dtype."""
        for start, end, step, dtype, expected, expected_dtype in self.test_cases:
            with self.subTest(start=start, end=end, step=step, dtype=dtype):
                result, = self.node.f(start, end, step, dtype)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected tensor values
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

                # Ensure result has the correct dtype
                self.assertEqual(result.dtype, expected_dtype, f"Expected dtype {expected_dtype}, got {result.dtype}")

if __name__ == "__main__":
    unittest.main()
