from typing import Any, Dict
import torch

class PtFloorDiv:
    """
    Performs element-wise floor division on two PyTorch tensors.

    category: PyTorch wrapper - Arithmetic operations
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the required input types.

        Returns:
            Dict[str, Any]: A dictionary of required input types.
        """
        return {
            "required": {
                "tens_a": ("TENSOR", {}),
                "tens_b": ("TENSOR", {})
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens_a: torch.Tensor, tens_b: torch.Tensor) -> tuple:
        """
        Performs element-wise floor division on two PyTorch tensors.

        Args:
            tens_a (torch.Tensor): A PyTorch tensor of any shape.
            tens_b (torch.Tensor): A PyTorch tensor of shape that supports element-wise floor division with `tens_a`.

        Returns:
            tuple: A tuple containing the resultant tensor.
        """
        return (torch.floor_divide(tens_a, tens_b),)
