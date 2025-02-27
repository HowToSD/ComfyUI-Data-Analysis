from typing import Any, Dict
import torch

class PtMm:
    """
    Performs 2D matrix multiplication on two PyTorch tensors.

    category: PyTorch wrapper - Matrix operations
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
        Performs 2D matrix multiplication on two PyTorch tensors.

        Args:
            tens_a (torch.Tensor): A 2D PyTorch tensor.
            tens_b (torch.Tensor): A 2D PyTorch tensor that supports matrix multiplication with `tens_a`.

        Returns:
            tuple: A tuple containing the resultant tensor.
        """
        if tens_a.dim() != 2 or tens_b.dim() != 2:
            raise ValueError("torch.mm() only supports 2D tensors.")

        return (torch.mm(tens_a, tens_b),)
