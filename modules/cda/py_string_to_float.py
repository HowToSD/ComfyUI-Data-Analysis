from typing import Any, Dict


class PyStringToFloat:
    """
    Converts a Python string to a float.

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
                "value": ("STRING", {"default":"", "multiline": False})
            }
        }

    RETURN_TYPES: tuple = ("FLOAT",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, value: str) -> tuple:
        """
        Converts a Python string to a float.
        
        Args:
            value (str): String value to convert.

        Returns:
            tuple: A tuple containing the dictionary.
        """
        return (float(value),)
    