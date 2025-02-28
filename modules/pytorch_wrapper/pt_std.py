from typing import Any, Dict
import torch
from .utils import str_to_dim


class PtStd:
    """
    Computes the standard deviation of a PyTorch tensor along the specified dimension(s).

    Specify 1 to use Bessel's correction (N-1) for sample standard deviation.
    Specify 0 to compute population standard deviation.

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
                "correction": ("INT", {"default": 1, "min": 0, "max": 1}),
                "dim": ("STRING", {"multiline": True}),
                "keepdim": ("BOOLEAN", {"default": False})
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor, dim: str, correction: int, keepdim: bool) -> tuple:
        """
        Computes the standard deviation along the specified dimension(s).

        Args:
            tens (torch.Tensor): The input tensor.
            dim (str): A string representation of the dimension(s) along which to compute the standard deviation,
                       e.g., "0", "[0]", or "(1, 2)".
            correction (int): 0 for population standard deviation, 1 for sample standard deviation (Bessel's correction).
            keepdim (bool): Whether to retain reduced dimensions.

        Returns:
            tuple: A tuple containing the standard deviation tensor.
        """
        dim = str_to_dim(dim)

        # Ensure correction is valid (0 or 1)
        if correction not in (0, 1):
            raise ValueError(f"Invalid correction value: {correction}. Must be 0 (population) or 1 (sample).")

        # Ensure keepdim is a boolean
        if not isinstance(keepdim, bool):
            raise TypeError(f"Invalid type for keepdim: {keepdim}. Must be a boolean.")

        # Compute the standard deviation along the specified dimension(s)
        tens = torch.std(tens, dim=dim, correction=correction, keepdim=keepdim)

        return (tens,)
