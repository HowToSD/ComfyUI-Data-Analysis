from typing import Any, Dict
import ast

class PyStringToDict:
    """
    Creates a Python dictionary using the string values entered in the text field.

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
                "data": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES: tuple = ("PYDICT",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, data: str) -> tuple:
        """
        Creates a Python dictionary using the string values entered in the text field.
        
        Args:
            data (str): String value in the text field.

        Returns:
            tuple: A dict converted from the input string.
        """
        d = ast.literal_eval(data)
        return (d,)

