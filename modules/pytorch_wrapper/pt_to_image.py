from typing import Any, Dict
import torch


class PtToImage:
    """
    Casts a PyTorch tensor as an Image tensor.

    category: PyTorch wrapper
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
            }
        }

    RETURN_TYPES: tuple = ("IMAGE",)
    FUNCTION: str = "f"
    CATEGORY: str = "PyTorch wrapper"

    def f(self, tens: torch.Tensor) -> tuple:
        """
        Casts a PyTorch tensor as an Image tensor.

        Args:
            tens (torch.Tensor): PyTorch Tensor

        Returns:
            tuple: A tuple containing the image tensor.
        """
        return (tens,)
