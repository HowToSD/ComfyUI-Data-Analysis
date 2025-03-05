from typing import Any, Dict
import torch


class PtFlatten:
    """
    Flattens a PyTorch tensor into a 1D tensor.

    category: PyTorch wrapper - Transform
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
                "tens": ("TENSOR", {}),
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor) -> tuple:
        """
        Flattens a PyTorch tensor into a 1D tensor.

        Args:
            tens (torch.Tensor): A PyTorch tensor of any shape.

        Returns:
            tuple: A tuple containing the flattened tensor.
        """
        return (tens.flatten(),)
