from typing import Any, Dict


class PyKvFloatCreate:
    """
    Creates a Python dictionary with a string key and a float value.

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
                "key": ("STRING", {"multiline": False}),
                "value": ("FLOAT", {"default": 0, "min": -2**63, "max": 2**63, "step": 0.00000001})
            }
        }

    RETURN_TYPES: tuple = ("PYDICT",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, key: str, value: float) -> tuple:
        """
        Creates a Python dictionary with a string key and a float value.
        
        Args:
            key (str): String key for the dictionary.
            value (float): Float value for the dictionary.

        Returns:
            tuple: A tuple containing the dictionary.
        """
        return ({key:value},)
    