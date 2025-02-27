from typing import Any, Dict, Tuple
import numpy as np
import torch


class PtFromNumpy:
    """
    Converts a NumPy ndarray to a PyTorch tensor while preserving its data type.

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
                "array": ("NDARRAY", {}),
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, array: np.ndarray) -> Tuple[torch.Tensor]:
        """
        Converts a NumPy ndarray to a PyTorch tensor while preserving its data type.

        Args:
            array (np.ndarray): NumPy ndarray.

        Returns:
            tuple: A tuple containing the PyTorch tensor.
        """
        tens = torch.tensor(array, dtype=torch.from_numpy(array).dtype)
        return (tens,)
