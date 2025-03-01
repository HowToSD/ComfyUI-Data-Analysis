from typing import Any, Dict
import numpy as np


class NumpySqueeze:
    """
    Removes a dimension at the specified position in the input array if it is of size 1.
    
    Specifying a tuple of dimensions is not supported.
    
    category: Numpy
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
                "dim": ("INT", {"default": -1, "min": -1, "max": 10})
            }
        }

    RETURN_TYPES: tuple = ("NDARRAY",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, array: np.ndarray, dim: int) -> tuple:
        """
        Removes a dimension at the specified position in the input array if it is of size 1.

        Args:
            array (np.ndarray): Input array.
            dim (int): Dimension to remove if it is of size 1.

        Returns:
            tuple: A tuple containing the transformed NumPy array.
        """
        ar_out = np.squeeze(array, dim)
        return (ar_out,)
