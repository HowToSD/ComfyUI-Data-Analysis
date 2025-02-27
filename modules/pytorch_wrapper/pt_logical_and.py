from typing import Any, Dict
import torch

class PtLogicalAnd:
    """
    Performs a logical AND operation on two PyTorch tensors element-wise.

    category: PyTorch wrapper - Logical operations
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
        Performs a logical AND operation on two PyTorch tensors.

        Args:
            tens_a (torch.Tensor): A PyTorch tensor of boolean or numerical type.
            tens_b (torch.Tensor): A PyTorch tensor of the same shape and type as `tens_a`.

        Returns:
            tuple: A tuple containing a boolean tensor where `tens_a AND tens_b` is applied element-wise.
        """
        return (torch.logical_and(tens_a, tens_b),)
