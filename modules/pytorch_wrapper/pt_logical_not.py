from typing import Any, Dict
import torch

class PtLogicalNot:
    """
    Performs a logical NOT operation on a PyTorch tensor element-wise.

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
                "tens_a": ("TENSOR", {})
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens_a: torch.Tensor) -> tuple:
        """
        Performs a logical NOT operation on a PyTorch tensor.

        Args:
            tens_a (torch.Tensor): A PyTorch tensor of boolean or numerical type.

        Returns:
            tuple: A tuple containing the resultant tensor after applying logical NOT.
        """
        return (torch.logical_not(tens_a),)
