from typing import Any, Dict
import torch
import ast


class PtSize:
    """
    Extracts the PyTorch Size object of a PyTorch tensor using the size() method.
    
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
                "tens": ("TENSOR",),
            }
        }

    RETURN_TYPES: tuple = ("PTSIZE",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor) -> tuple:
        """
        Extracts the PyTorch Size object of a PyTorch tensor using the size() method.

        Args:
            tens (torch.Tensor): The tensor.

        Returns:
            tuple: A tuple containing the PyTorch Size.
        """
        return (tens.size(),)
