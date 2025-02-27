from typing import Any, Dict
import torch


class PtFromLatent:
    """
    Casts a latent tensor as a PyTorch tensor.

    category: PyTorch wrapper - Tensor creation
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
                "latent": ("LATENT", {}),
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, latent: torch.Tensor) -> tuple:
        """
        Casts a latent tensor as a PyTorch tensor.

        Args:
            latent (torch.Tensor): Latent tensor

        Returns:
            tuple: A tuple containing the PyTorch tensor.
        """
        return (latent["samples"],)
