from typing import Any, Dict
import torch

class PtPow:
    """
    Raises one PyTorch tensor to the power of another element-wise.

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
        Raises one PyTorch tensor to the power of another element-wise.

        Args:
            tens_a (torch.Tensor): A PyTorch tensor of any shape.
            tens_b (torch.Tensor): A PyTorch tensor of shape that supports element-wise exponentiation with `tens_a`.

        Returns:
            tuple: A tuple containing the resultant tensor.
        """
        return (torch.pow(tens_a, tens_b),)
