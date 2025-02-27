from typing import Any, Dict
import torch


class PtUnsqueeze:
    """
    Adds a singleton dimension at the specified position in the input tensor.
    For example, if a tensor has shape (3, 4) and `dim=1`, the output will have shape (3, 1, 4).
    
    category: PyTorch wrapper - Transform
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "tens": ("TENSOR", {}),
                "dim": ("INT", {"default": -1, "min": -10, "max": 10})
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor, dim: int) -> tuple:
        """
        Adds a singleton dimension at the specified position.

        Args:
            tens (torch.Tensor): Input tensor.
            dim (int): Dimension at which to insert the new singleton dimension.

        Returns:
            tuple: A tuple containing the transformed PyTorch tensor.
        """
        tens = torch.unsqueeze(tens, dim)
        return (tens,)
