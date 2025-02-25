import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_size_to_string import PtSizeToString

class TestPtSizeToString(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PtSizeToString()

        # Test cases with torch.Size objects
        self.test_cases = [
            # Empty size (zero-rank tensor shape)
            (torch.Size([]), "torch.Size([])"),
            # Rank 1 (single-dimension size)
            (torch.Size([3]), "torch.Size([3])"),
            # Rank 2 (matrix size)
            (torch.Size([3, 4]), "torch.Size([3, 4])"),
            # Rank 3 (3D tensor size)
            (torch.Size([2, 3, 4]), "torch.Size([2, 3, 4])"),
            # Rank 4 (higher-dimensional tensor size)
            (torch.Size([1, 2, 3, 4]), "torch.Size([1, 2, 3, 4])"),
            # Rank 5 (very high-dimensional tensor size)
            (torch.Size([5, 4, 3, 2, 1]), "torch.Size([5, 4, 3, 2, 1])"),
        ]

    def test_convert_size_to_string(self):
        """Test conversion of PyTorch Size to string."""
        for torch_size, expected_string in self.test_cases:
            with self.subTest(data=torch_size):
                retval = self.node.f(torch_size)[0]

                # Ensure the returned value is a string
                self.assertTrue(isinstance(retval, str), f"Expected str, got {type(retval)}")

                # Ensure the value matches expected string
                self.assertEqual(retval, expected_string, f"Value mismatch for input: {torch_size}")

if __name__ == "__main__":
    unittest.main()
