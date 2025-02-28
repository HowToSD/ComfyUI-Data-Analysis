from typing import Any, Dict
import torch
from .utils import str_to_dim


class PtMedian:
    """
    Computes the median of a PyTorch tensor along the specified dimension(s).

    Specify the dimension(s) in the `dim` field using an integer as shown below:
    ```
    0
    ```
    or
    ```
    1
    ```    
    Note that PtMedian calls torch.median(), which returns the lower of the two numbers when the true median falls between them.

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
        Computes the median along the specified dimension(s).

        Args:
            tens (torch.Tensor): The input tensor.
            dim (str): A string representation of the dimension(s) along which to compute the median,
                       e.g., "0", or "1".
            keepdim (bool): Whether to retain reduced dimensions.

        Returns:
            tuple: A tuple containing the median tensor.
        """
        dim = str_to_dim(dim)
        if not isinstance(dim, int):
            raise TypeError(f"Invalid type for dim: {dim}. Must be a integer.")
        # Ensure keepdim is a boolean
        if not isinstance(keepdim, bool):
            raise TypeError(f"Invalid type for keepdim: {keepdim}. Must be a boolean.")

        # Compute the median along the specified dimension(s)
        tens, _ = torch.median(tens, dim=dim, keepdim=keepdim)

        return (tens,)
