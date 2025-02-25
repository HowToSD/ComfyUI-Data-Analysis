from typing import Any, Dict
import torch


class PtFromImage:
    """
    Casts an Image tensor as a PyTorch tensor.

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
                "image": ("IMAGE", {}),
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "PyTorch wrapper"

    def f(self, image: torch.Tensor) -> tuple:
        """
        Casts an Image tensor as a PyTorch tensor.

        Args:
            image (torch.Tensor): Image tensor

        Returns:
            tuple: A tuple containing the PyTorch tensor.
        """
        return (image,)
