from typing import Any, Dict
import pandas as pd
import torch


class PandasCreateFromTensor:
    """
    Creates a pandas DataFrame from a PyTorch tensor.

    category: IO
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `create` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "tens": ("TENSOR", {}),
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor) -> tuple:
        """
        Creates a pandas DataFrame from a PyTorch tensor.

        Args:
            tens (torch.Tensor): A PyTorch tensor.

        Returns:
            tuple: A tuple containing the DataFrame.
        
        Raises:
            ValueError: If the tensor is not rank 1 or rank 2.
        """
        if tens.dim() not in [1, 2]:
            raise ValueError("Only rank 1 and rank 2 tensors are supported.")

        return (pd.DataFrame(tens.numpy()),)

