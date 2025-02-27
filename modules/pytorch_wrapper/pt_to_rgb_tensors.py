from typing import Any, Dict
import torch


class PtToRgbTensors:
    """
    Splits a PyTorch tensor into R, G, and B tensors.

    category: PyTorch wrapper - Tensor data conversion
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

    RETURN_NAMES: tuple = ("R", "G", "B")
    RETURN_TYPES: tuple = ("TENSOR", "TENSOR", "TENSOR")
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor) -> tuple:
        """
        Splits a PyTorch tensor into R, G, and B tensors.

        Args:
            tens (torch.Tensor): A PyTorch tensor of shape [B, H, W, C] or [H, W, C].
                                 Assumes the last axis represents the color channels.

        Returns:
            tuple: A tuple containing the R, G, and B tensors.
                   If the input tensor has a batch axis, it will be retained.
        
        Raises:
            ValueError: If the input tensor does not have exactly 3 channels.
        """
        if tens.size()[-1] != 3:
            raise ValueError(f"Expected a 3-channel tensor, but got {tens.size()[-1]} channels.")

        r, g, b = tens[..., 0], tens[..., 1], tens[..., 2]
        return (r, g, b)
