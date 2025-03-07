from typing import Any, List
import ast

class PyStringToList:
    """
    Creates a Python list using the string values entered in the text field.

    category: Python wrapper
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> List[str]:
        """
        Defines the input types for the `create` function.

        Returns:
            List[str, Any]: A list specifying required input types.
        """
        return {
            "required": {
                "data": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES: tuple = ("PYLIST",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, data: str) -> tuple:
        """
        Creates a Python list using the string values entered in the text field.
        
        Args:
            data (str): String value in the text field.

        Returns:
            tuple: A list converted from the input string.
        """
        d = ast.literal_eval(data)
        return (d,)

