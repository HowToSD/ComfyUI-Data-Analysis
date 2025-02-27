from typing import Any, Dict
import torch
import ast


class PtSizeCreate:
    """
    Creates a PyTorch Size using values entered in the text field.
    
    category: PyTorch wrapper - Size object support
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

    RETURN_TYPES: tuple = ("PTSIZE",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, data: str) -> tuple:
        """
        Creates a PyTorch Size using values entered in the text field.

        Args:
            data (str): String value in the text field.

        Returns:
            tuple: A tuple containing the PyTorch Size.
        """
        # Convert string to Python list
        list_data = ast.literal_eval(data)

        # Convert list to PyTorch Size
        size = torch.Size(list_data)
        return (size,)
