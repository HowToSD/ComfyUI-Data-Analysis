from typing import Any, Dict
import torch
import ast


class PtFloatCreate:
    """
    Creates a PyTorch tensor with 32-bit floating point precision 
    using values entered in the text field.
    
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
                "data": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, data: str) -> tuple:
        """
        Creates a PyTorch tensor using values entered in the text field.

        Args:
            data (str): String value in the text field.

        Returns:
            tuple: A tuple containing the tensor.
        """
        # Convert string to Python list
        list_data = ast.literal_eval(data)

        # Convert list to PyTorch tensor
        tensor = torch.tensor(list_data, dtype=torch.float32)
        return (tensor,)
