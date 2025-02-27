import os
import sys
import unittest
import torch


PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_full import PtFull
from pytorch_wrapper.utils import DTYPE_MAPPING


class TestPtFull(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtFull()

        # Tensor size to test
        self.size_str = "[2, 3]"  # Using a small 2D tensor size for all tests
        self.expected_shape = (2, 3)

        # Values to test (using representative values for each type)
        self.test_values = {
            "float32": "1.5",
            "float16": "-2.3",
            "bfloat16": "3.7",
            "float64": "4.9",
            "uint8": "255",  # Max value for uint8
            "int8": "-128",  # Min value for int8
            "int16": "32767",  # Max value for int16
            "int32": "-2147483648",  # Min value for int32
            "int64": "9223372036854775807",  # Max value for int64
            "bool": "True"
        }

    def test_full_tensor_all_dtypes(self):
        """Test tensor creation with a specified value for all supported data types."""
        for data_type, torch_dtype in DTYPE_MAPPING.items():
            value_str = self.test_values[data_type]

            with self.subTest(data_type=data_type, value=value_str):
                result, = self.node.f(value_str, self.size_str, data_type)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result has correct shape
                self.assertEqual(result.shape, torch.Size(self.expected_shape), f"Expected shape {self.expected_shape}, got {result.shape}")

                # Ensure result has correct dtype
                self.assertEqual(result.dtype, torch_dtype, f"Expected dtype {torch_dtype}, got {result.dtype}")

                # Convert value_str to correct type
                if torch_dtype in {torch.float32, torch.float16, torch.bfloat16, torch.float64}:
                    expected_value = float(value_str)
                elif torch_dtype in {torch.uint8, torch.int8, torch.int16, torch.int32, torch.int64}:
                    expected_value = int(value_str)
                elif torch_dtype == torch.bool:
                    expected_value = value_str.lower() == "true"
                else:
                    raise ValueError(f"Unsupported data type: {data_type}")

                # Ensure all elements match the expected value
                expected = torch.full(self.expected_shape, expected_value, dtype=torch_dtype)
                self.assertTrue(torch.equal(result, expected), f"Tensor values do not match expected tensor for dtype {data_type}")


if __name__ == "__main__":
    unittest.main()
