import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_linspace import PtLinspace


class TestPtLinspace(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtLinspace()

        # Test cases: (start, end, steps, dtype, expected_tensor, expected_dtype)
        self.test_cases = [
            ("0", "10", "5", "float32", torch.tensor([0, 2.5, 5, 7.5, 10], dtype=torch.float32), torch.float32),  # Basic float32 case
            ("-5", "5", "6", "float64", torch.tensor([-5, -3, -1, 1, 3, 5], dtype=torch.float64), torch.float64),  # Negative to positive
            ("1", "2", "3", "float16", torch.tensor([1, 1.5, 2], dtype=torch.float16), torch.float16),  # Small float16 case
            ("100", "200", "5", "int32", torch.tensor([100, 125, 150, 175, 200], dtype=torch.int32), torch.int32),  # Large int32 case
            ("0", "1", "2", "bfloat16", torch.tensor([0, 1], dtype=torch.bfloat16), torch.bfloat16),  # Simple two-step bfloat16
        ]

    def test_linspace_tensor_creation(self):
        """Test tensor generation using torch.linspace(), including values and dtype."""
        for start, end, steps, dtype, expected, expected_dtype in self.test_cases:
            with self.subTest(start=start, end=end, steps=steps, dtype=dtype):
                result, = self.node.f(start, end, steps, dtype)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected tensor values
                self.assertTrue(torch.allclose(result, expected, atol=1e-5), f"Expected {expected}, got {result}")

                # Ensure result has the correct dtype
                self.assertEqual(result.dtype, expected_dtype, f"Expected dtype {expected_dtype}, got {result.dtype}")

if __name__ == "__main__":
    unittest.main()
