from typing import Any, Dict
import torch


class PtToLatent:
    """
    Casts a PyTorch tensor as a latent tensor.

    category: PyTorch wrapper - Tensor data conversion
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

    RETURN_TYPES: tuple = ("LATENT",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor) -> tuple:
        """
        Casts a PyTorch tensor as a latent tensor.

        Args:
            tens (torch.Tensor): PyTorch Tensor

        Returns:
            tuple: A tuple containing the latent tensor.
        """
        return ({"samples":tens},)
