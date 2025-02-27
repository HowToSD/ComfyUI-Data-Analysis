from typing import Any, Dict
import torch
from .utils import DTYPE_MAPPING

class PtSqueeze:
    """
    Removes a dimension at the specified position in the input tensor if it is of size 1.
    
    Specifying a tuple of dimensions is not supported yet.
    
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
                "dim": ("INT", {"default": -1, "min": -1, "max": 10})
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor, dim: int) -> tuple:
        """
        Removes a dimension at the specified position in the input tensor if it is of size 1.

        Args:
            tens (torch.Tensor): Input tensor.
            dim (int): Dimension to remove if it is of size 1.

        Returns:
            tuple: A tuple containing the transformed PyTorch tensor.
        """
        tens = torch.squeeze(tens, dim)
        return (tens,)
