import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_size import PtSize

class TestPtSize(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PtSize()

        # Test cases with torch.Tensor objects
        self.test_cases = [
            # Rank 0 (scalar tensor)
            (torch.tensor(42), torch.Size([])),
            # Rank 1 (vector tensor)
            (torch.tensor([1, 2, 3]), torch.Size([3])),
            # Rank 2 (matrix tensor)
            (torch.tensor([[1, 2], [3, 4]]), torch.Size([2, 2])),
            # Rank 3 (3D tensor)
            (torch.tensor([[[1], [2]], [[3], [4]]]), torch.Size([2, 2, 1])),
            # Rank 4 (4D tensor)
            (torch.tensor([[[[1, 2], [3, 4]]]]), torch.Size([1, 1, 2, 2])),
        ]

    def test_extract_size(self):
        """Test PyTorch Size extraction from tensors."""
        for tensor, expected_size in self.test_cases:
            with self.subTest(data=tensor):
                retval = self.node.f(tensor)[0]

                # Ensure the returned value is a PyTorch Size
                self.assertTrue(isinstance(retval, torch.Size), f"Expected Size, got {type(retval)}")

                # Ensure the value matches expected size
                self.assertEqual(retval, expected_size, f"Value mismatch for input: {tensor}")

if __name__ == "__main__":
    unittest.main()
