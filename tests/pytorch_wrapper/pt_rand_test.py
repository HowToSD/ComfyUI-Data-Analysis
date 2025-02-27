import os
import sys
import unittest
import torch


PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_rand import PtRand  # Importing the PtRand class
from pytorch_wrapper.utils import DTYPE_MAPPING  # Importing the dtype mapping


class TestPtRand(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtRand()

        # Tensor size to test
        self.size_str = "[2, 3]"  # Using a small 2D tensor size for all tests
        self.expected_shape = (2, 3)

        # Only floating-point types are valid for torch.rand()
        self.valid_dtypes = {k: v for k, v in DTYPE_MAPPING.items() if v in {torch.float32, torch.float16, torch.bfloat16, torch.float64}}

    def test_rand_tensor_all_floating_dtypes(self):
        """Test random tensor creation for all supported floating-point data types."""
        for data_type, torch_dtype in self.valid_dtypes.items():
            with self.subTest(data_type=data_type):
                result, = self.node.f(self.size_str, data_type)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result has correct shape
                self.assertEqual(result.shape, torch.Size(self.expected_shape), f"Expected shape {self.expected_shape}, got {result.shape}")

                # Ensure result has correct dtype
                self.assertEqual(result.dtype, torch_dtype, f"Expected dtype {torch_dtype}, got {result.dtype}")

                # Ensure all elements are within range [0,1)
                self.assertTrue(torch.all(result >= 0) and torch.all(result < 1), f"Tensor values are not in the range [0,1) for dtype {data_type}")

if __name__ == "__main__":
    unittest.main()
