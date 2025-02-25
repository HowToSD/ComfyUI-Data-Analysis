from typing import Any, Dict
import torch


class PtToNumpy:
    """
    Converts PyTorch tensor to NumPy ndarray.

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

    RETURN_TYPES: tuple = ("NDARRAY",)
    FUNCTION: str = "f"
    CATEGORY: str = "PyTorch wrapper"

    def f(self, tens: torch.Tensor) -> tuple:
        """
        Converts PyTorch tensor to NumPy ndarray.

        Args:
            tens (torch.Tensor): PyTorch Tensor

        Returns:
            tuple: A tuple containing the ndarray.
        """
        array = tens.cpu().detach().numpy()
        return (array,)
