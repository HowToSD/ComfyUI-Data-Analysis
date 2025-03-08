from typing import Any, Dict
import torch


class PtToImageTranspose:
    """
    Casts a PyTorch tensor as an Image tensor and transposes it from (C, H, W) to (H, W, C). For rank-4 inputs, the batch axis remains unchanged.

    category: PyTorch wrapper - Image processing
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

    RETURN_NAMES: tuple = ("image",)
    RETURN_TYPES: tuple = ("IMAGE",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor) -> tuple:
        """
        Casts a PyTorch tensor as an Image tensor.

        Args:
            tens (torch.Tensor): PyTorch Tensor

        Returns:
            tuple: A tuple containing the image tensor.
        """
        if tens.dim() == 3:
            image = tens.permute(1, 2, 0)
        elif tens.dim() == 4:
            image = tens.permute(0, 2, 3, 1)
        else:
            raise ValueError("Only rank 3 or 4 tensors are supported.")
        return (image,)
