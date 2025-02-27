from typing import Any, Dict
import torch

class PtEq:
    """
    Tests whether two PyTorch tensors are equal element-wise.

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
        Compares two PyTorch tensors for element-wise equality.

        Args:
            tens_a (torch.Tensor): A PyTorch tensor of any shape.
            tens_b (torch.Tensor): A PyTorch tensor of the same shape as `tens_a`.

        Returns:
            tuple: A tuple containing a boolean tensor indicating element-wise equality.
        """
        return (torch.eq(tens_a, tens_b),)
