from typing import Any, Dict
import torch
import ast


class PtBoolCreate:
    """
    Creates a PyTorch tensor of dtype bool from True or False values entered as a list in the text field.
    For example, entering:
    ```
    [True, False, False]
    ```
    will create a 1D boolean tensor.
    
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
        Creates a PyTorch tensor with bool data type using True or False string values entered in the text field.

        Args:
            data (str): String value in the text field.

        Returns:
            tuple: A tuple containing the tensor.
        """
        # Convert string to Python list
        list_data = ast.literal_eval(data)

        # Convert list to PyTorch tensor
        tensor = torch.tensor(list_data, dtype=torch.bool)
        return (tensor,)
