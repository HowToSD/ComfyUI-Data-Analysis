from typing import Any, Dict
import torch

class PtGe:
    """
    Tests whether elements in the first PyTorch tensor are greater than or equal to the corresponding elements in the second tensor.

    category: PyTorch wrapper - Comparison operations
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
        Compares two PyTorch tensors for element-wise greater-than-or-equal-to condition.

        Args:
            tens_a (torch.Tensor): A PyTorch tensor of any shape.
            tens_b (torch.Tensor): A PyTorch tensor of the same shape as `tens_a`.

        Returns:
            tuple: A tuple containing a boolean tensor indicating where `tens_a >= tens_b`.
        """
        return (torch.ge(tens_a, tens_b),)
