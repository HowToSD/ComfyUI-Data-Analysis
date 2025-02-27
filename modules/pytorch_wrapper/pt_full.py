from typing import Any, Dict
import torch
import ast
from .utils import DTYPE_MAPPING

class PtFull:
    """
    Creates a PyTorch tensor filled with a specified value using the size entered in the text field.
    For example, if you want to create a 4D tensor of batch size=2, channel=3, height=96, width=32 filled with 7, enter:
    [2,3,96,32] for size and 7 for value.
    
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
                "value": ("STRING", {"multiline": False}),
                "size": ("STRING", {"multiline": True}),
                "data_type": (("float32", "float16", "bfloat16", "float64", "uint8", "int8", "int16", "int32", "int64", "bool"),)
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, value: str, size: str, data_type: str) -> tuple:
        """
        Creates a PyTorch tensor filled with a specified value.

        Args:
            value (str): String representing the value to fill the tensor.
            size (str): String representation of the tensor size.
            data_type (str): Desired data type of the tensor.

        Returns:
            tuple: A tuple containing the PyTorch tensor.
        """
        # Convert string to Python list
        list_size = ast.literal_eval(size)

        # Convert the value to the appropriate type
        dtype = DTYPE_MAPPING[data_type]
        
        if dtype in {torch.float32, torch.float16, torch.bfloat16, torch.float64}:
            fill_value = float(value)
        elif dtype in {torch.uint8, torch.int8, torch.int16, torch.int32, torch.int64}:
            fill_value = int(value)
        elif dtype == torch.bool:
            fill_value = value.lower() in {"true", "1"}
        else:
            raise ValueError(f"Unsupported data type: {data_type}")

        # Convert list to PyTorch Size
        sz = torch.Size(list_size)
        tens = torch.full(sz, fill_value, dtype=dtype)

        return (tens,)
