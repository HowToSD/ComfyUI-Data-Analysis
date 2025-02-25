from typing import Any, Dict
import pandas as pd
import numpy as np


class PandasCreateFromNumpy:
    """
    Creates a pandas DataFrame from a NumPy ndarray.

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
                "data": ("NDARRAY", {}),
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, data: np.ndarray) -> tuple:
        """
        Creates a pandas DataFrame from a NumPy ndarray.

        Args:
            data (np.ndarray): A NumPy array.

        Returns:
            tuple: A tuple containing the DataFrame.
        
        Raises:
            ValueError: If the array is not rank 1 or rank 2.
        """
        if len(data.shape) not in [1, 2]:
            raise ValueError("Only rank 1 and rank 2 arrays are supported.")

        return (pd.DataFrame(data),)

