from typing import Any, Dict
import torch

class PtTanh:
    """
    Computes the hyperbolic tangent of a PyTorch tensor element-wise.

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
        Computes the element-wise hyperbolic tangent of a PyTorch tensor.

        Args:
            tens_a (torch.Tensor): A PyTorch tensor of numerical type.

        Returns:
            tuple: A tuple containing the resultant tensor after applying the hyperbolic tangent function.
        """
        return (torch.tanh(tens_a),)
