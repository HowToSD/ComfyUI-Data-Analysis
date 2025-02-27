import time
from typing import Any, Dict
import torch
import ast
import copy
from .utils import DTYPE_MAPPING

class PtRandInt:
    """
    Creates a PyTorch tensor filled with random integers within a specified range using the size entered in the text field.
    For example, if you want to create a 4D tensor of batch size=2, channel=3, height=96, width=32 with random integers in the range [0, 10),
    enter [2,3,96,32] for size, 0 for min_value, and 10 for max_value.
    
    category: PyTorch wrapper - Tensor creation
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "min_value": ("INT", {"default": 0, "min": -2**31, "max": 2**31}),
                "max_value": ("INT", {"default": 1, "min": -2**31, "max": 2**31}),
                "size": ("STRING", {"multiline": True}),
                "data_type": (("uint8", "int8", "int16", "int32", "int64"),)
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def __init__(self):
        # Initialize a separate generator with a different seed
        self.gen = torch.Generator()
        self.gen.manual_seed(int(time.time() * 1000000) % (2**32))  # Unique seed

    def f(self, min_value: int, max_value: int, size: str, data_type: str) -> tuple:
        """
        Creates a PyTorch tensor filled with random integers in the range [min_value, max_value).

        Args:
            min_value (int): Minimum value (inclusive).
            max_value (int): Maximum value (exclusive).
            size (str): String representation of the tensor size.
            data_type (str): Desired integer data type of the tensor.

        Returns:
            tuple: A tuple containing the PyTorch tensor.
        """
        # Convert string to Python list
        list_size = ast.literal_eval(size)

        # Convert list to PyTorch Size
        sz = torch.Size(list_size)

        # Ensure max_value is greater than min_value
        if max_value <= min_value:
            raise ValueError("max_value must be greater than min_value.")

        # Generate random integers within the specified range
        tens = torch.randint(min_value, max_value, sz, dtype=DTYPE_MAPPING[data_type], generator=self.gen)
        return (tens,)
