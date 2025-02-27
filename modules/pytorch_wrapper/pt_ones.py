from typing import Any, Dict
import torch
import ast
from .utils import DTYPE_MAPPING

class PtOnes:
    """
    Creates a PyTorch tensor of ones using the size entered in the text field.
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
                "data_type": (("float32", "float16", "bfloat16", "float64", "uint8", "int8", "int16", "int32", "int64", "bool"),)
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, size: str, data_type: str) -> tuple:
        """
        Creates a PyTorch tensor of ones using the size entered in the text field.

        Args:
            size (str): String value in the text field.
            data_type (str): Desired data type of the tensor.

        Returns:
            tuple: A tuple containing the PyTorch tensor.
        """
        # Convert string to Python list
        list_size = ast.literal_eval(size)

        # Convert list to PyTorch Size
        sz = torch.Size(list_size)

        tens = torch.ones(sz, dtype=DTYPE_MAPPING[data_type])

        return (tens,)
