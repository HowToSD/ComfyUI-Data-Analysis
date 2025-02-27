from typing import Any, Dict
import torch

class PtBitwiseOr:
    """
    Performs a bitwise OR operation on two PyTorch tensors element-wise.

    category: PyTorch wrapper - Bitwise operations
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
        Performs a bitwise OR operation on two PyTorch tensors.

        Args:
            tens_a (torch.Tensor): A PyTorch tensor of integer type.
            tens_b (torch.Tensor): A PyTorch tensor of the same shape and integer type as `tens_a`.

        Returns:
            tuple: A tuple containing the resultant tensor after applying bitwise OR.
        """
        return (torch.bitwise_or(tens_a, tens_b),)
