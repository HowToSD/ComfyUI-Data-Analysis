from typing import Any, Dict
import torch

class PtLog:
    """
    Computes the natural logarithm (log base e) of a PyTorch tensor element-wise.

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
        Computes the element-wise natural logarithm (log base e) of a PyTorch tensor.

        Args:
            tens_a (torch.Tensor): A PyTorch tensor of numerical type. Must contain only positive values.

        Returns:
            tuple: A tuple containing the resultant tensor after applying the natural logarithm.
        """
        return (torch.log(tens_a),)
