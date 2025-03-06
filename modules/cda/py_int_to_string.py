from typing import Any, Dict


class PyIntToString:
    """
    Converts a Python int value to a Python string

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
                "value": ("INT", {"default": 0, "min": -2**31, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, value: int) -> tuple:
        """
        Converts a Python int value to a Python string

        Args:
            value (int): Int value to convert.

        Returns:
            tuple: A tuple containing the converted value.
        """
        return (str(value),)
    