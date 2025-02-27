from typing import Any, Dict
import torch

class PtNeg:
    """
    Computes the negation of each element in a PyTorch tensor.

    category: PyTorch wrapper - Math operations
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
                "tens_a": ("TENSOR", {})
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens_a: torch.Tensor) -> tuple:
        """
        Computes the negation of a PyTorch tensor element-wise.

        Args:
            tens_a (torch.Tensor): A PyTorch tensor of numerical type.

        Returns:
            tuple: A tuple containing the resultant tensor after applying negation.
        """
        return (torch.neg(tens_a),)
