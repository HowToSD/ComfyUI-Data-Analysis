from typing import Any, Dict


class PyStringToInt:
    """
    Converts a Python string to an int.

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

    RETURN_TYPES: tuple = ("INT",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, value: str) -> tuple:
        """
        Converts a Python string to an int.
        
        Args:
            value (str): String value to convert.

        Returns:
            tuple: A tuple containing the dictionary.
        """
        return (int(value),)
    