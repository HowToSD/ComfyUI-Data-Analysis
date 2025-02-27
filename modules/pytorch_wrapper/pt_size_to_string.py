from typing import Any, Dict
import torch


class PtSizeToString:
    """
    Converts PyTorch Size object to a Python string.

    category: PyTorch wrapper - Size object support
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
                "sz": ("PTSIZE", {}),
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, sz: torch.Size) -> tuple:
        """
        Converts PyTorch Size object to a Python string.

        Args:
            sz (torch.Size): PyTorch Size

        Returns:
            tuple: A tuple containing the string.
        """
        return (str(sz),)
