from typing import Any, Dict
import torch


class PtFromImageTranspose:
    """
    Casts an image tensor to a PyTorch tensor and transposes it from (H, W, C) to (C, H, W). For rank-4 inputs, the batch axis remains unchanged.

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
                "image": ("IMAGE", {}),
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, image: torch.Tensor) -> tuple:
        """
        Casts an Image tensor as a PyTorch tensor.

        Args:
            image (torch.Tensor): Image tensor

        Returns:
            tuple: A tuple containing the PyTorch tensor.
        """
        if image.dim() == 3:
            tens = image.permute(2, 0, 1)
        elif image.dim() == 4:
            tens = image.permute(0, 3, 1, 2)
        else:
            raise ValueError("Only rank 3 or 4 tensors are supported.")

        return (tens,)
