from typing import Any, Dict
import torch
from .utils import str_to_dim


class PtMin:
    """
    Computes the minimum values of a PyTorch tensor along the specified dimension(s).

    Specify the dimension(s) in the `dim` field using an integer, a list, or a tuple, as shown below:
    ```
    0, [0], or (1, 2)
    ```
    category: PyTorch wrapper - Reduction operation & Summary statistics
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
                "dim": ("STRING", {"multiline": True}),
                "keepdim": ("BOOLEAN", {"default": False})
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor, dim: str, keepdim: bool) -> tuple:
        """
        Computes the minimum values along the specified dimension(s).

        Args:
            tens (torch.Tensor): The input tensor.
            dim (str): A string representation of the dimension(s) along which to compute the minimum,
                       e.g., "0", "[0]", or "(1, 2)".
            keepdim (bool): Whether to retain reduced dimensions.

        Returns:
            tuple: A tuple containing the tensor with minimum values.
        """
        dim = str_to_dim(dim)

        # Ensure keepdim is a boolean
        if not isinstance(keepdim, bool):
            raise TypeError(f"Invalid type for keepdim: {keepdim}. Must be a boolean.")

        # Compute the min along the specified dimension(s)
        tens = torch.amin(tens, dim=dim, keepdim=keepdim)

        return (tens,)
