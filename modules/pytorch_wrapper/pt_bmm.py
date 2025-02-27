from typing import Any, Dict
import torch

class PtBmm:
    """
    Performs batched matrix multiplication on two 3D PyTorch tensors.

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
        Performs batched matrix multiplication on two 3D PyTorch tensors.

        Args:
            tens_a (torch.Tensor): A 3D PyTorch tensor (batch, m, n).
            tens_b (torch.Tensor): A 3D PyTorch tensor (batch, n, p) that supports matrix multiplication with `tens_a`.

        Returns:
            tuple: A tuple containing the resultant 3D tensor.
        """
        if tens_a.dim() != 3 or tens_b.dim() != 3:
            raise ValueError("torch.bmm() only supports batch matrix multiplication for 3D tensors.")

        return (torch.bmm(tens_a, tens_b),)
