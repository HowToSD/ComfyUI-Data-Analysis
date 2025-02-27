import os
import sys
import unittest
import torch
import ast


PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_rand_int import PtRandInt  # Importing the PtRandInt class
from pytorch_wrapper.utils import DTYPE_MAPPING  # Importing the dtype mapping


class TestPtRandInt(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtRandInt()

        # Tensor size to test
        self.size_str = "[2, 3]"  # Using a small 2D tensor size for all tests
        self.expected_shape = (2, 3)

        # Only integer types are valid for torch.randint()
        self.valid_dtypes = {
            k: v for k, v in DTYPE_MAPPING.items() if v in {torch.int8, torch.int16, torch.int32, torch.int64, torch.uint8}
        }

        # Define min and max values for each integer type
        self.test_ranges = {
            "int8": (-128, 127),
            "int16": (-32768, 32767),
            "int32": (-2147483648, 2147483647),
            "int64": (-9223372036854775808, 9223372036854775807),
            "uint8": (0, 255),
        }

    def test_randint_tensor_all_integer_dtypes(self):
        """Test random integer tensor creation for all supported integer data types."""
        for data_type, torch_dtype in self.valid_dtypes.items():
            min_value, max_value = self.test_ranges[data_type]

            with self.subTest(data_type=data_type, min_value=min_value, max_value=max_value):
                result, = self.node.f(min_value, max_value, self.size_str, data_type)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result has correct shape
                self.assertEqual(result.shape, torch.Size(self.expected_shape), f"Expected shape {self.expected_shape}, got {result.shape}")

                # Ensure result has correct dtype
                self.assertEqual(result.dtype, torch_dtype, f"Expected dtype {torch_dtype}, got {result.dtype}")

                # Ensure all elements are within range [min_value, max_value)
                self.assertTrue(torch.all(result >= min_value), f"Tensor contains values less than min_value for dtype {data_type}")
                self.assertTrue(torch.all(result < max_value), f"Tensor contains values greater than or equal to max_value for dtype {data_type}")

if __name__ == "__main__":
    unittest.main()
