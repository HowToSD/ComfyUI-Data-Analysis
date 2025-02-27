from typing import Any, Dict
import numpy as np
import ast


class NumpyFloatCreate:
    """
    Creates a NumPy ndarray with 32-bit floating point precision 
    using values entered in the text field.
    
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
                "data": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES: tuple = ("NDARRAY",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, data: str) -> tuple:
        """
        Creates a Numpy ndarray using values entered in the text field.

        Args:
            data (str): String value in the text field.

        Returns:
            tuple: A tuple containing a the DataFrame.
        """
        # Convert string to Python list
        list_data = ast.literal_eval(data)

        # Convert list to NumPy array
        array = np.array(list_data, dtype=np.float32)
        return (array,)
