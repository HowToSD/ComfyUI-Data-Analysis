from typing import Any, Dict
import datetime

class PyFloatToString:
    """
    Converts a Python float value to a Python string

    category: Python wrapper
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
                "value": ("FLOAT", {"default": 0, "min": -2**63, "max": 2**63, "step": 0.00000001})
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, value: float) -> tuple:
        """
        Converts a Python float value to a Python string

        Args:
            value (float): Float value to convert.

        Returns:
            tuple: A tuple containing the converted value.
        """
        return (str(value),)
    