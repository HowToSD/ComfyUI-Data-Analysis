from typing import Any, Dict, List

class PyListToString:
    """
    Converts a Python list value to a Python string

    category: Python wrapper
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
                "value": ("PYLIST", {})
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, value: List) -> tuple:
        """
        Converts a Python list value to a Python string

        Args:
            value (list): List value to convert.

        Returns:
            tuple: A tuple containing the converted value.
        """
        return (str(value),)
    