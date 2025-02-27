from typing import Any, Dict
import torch
import ast
from .utils import DTYPE_MAPPING

class PtRandn:
    """
    Creates a PyTorch tensor with values sampled from a standard normal distribution (mean=0, std=1) 
    using the size entered in the text field.
    For example, if you want to create a 4D tensor of batch size=2, channel=3, height=96, width=32, enter:
    [2,3,96,32]
    
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
                "size": ("STRING", {"multiline": True}),
                "data_type": (("float32", "float16", "bfloat16", "float64"),)
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def f(self, size: str, data_type: str) -> tuple:
        """
        Creates a PyTorch tensor with values sampled from a standard normal distribution.

        Args:
            size (str): String value in the text field.
            data_type (str): Desired floating-point data type of the tensor.

        Returns:
            tuple: A tuple containing the PyTorch tensor.
        """
        # Convert string to Python list
        list_size = ast.literal_eval(size)

        # Convert list to PyTorch Size
        sz = torch.Size(list_size)
        tens = torch.randn(sz, dtype=DTYPE_MAPPING[data_type])

        return (tens,)
