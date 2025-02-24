from typing import Any, Dict


class PyKvIntCreate:
    """
    Creates a Python dictionary with an string key and an integer value.

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
                "value": ("INT", {"default": 0, "min": -2**31, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("PYDICT",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, key: str, value: int) -> tuple:
        """
        Creates a Python dictionary with an string key and an integer value.
        
        Args:
            key (str): String key for the dictionary.
            value (int): Integer value for the dictionary.

        Returns:
            tuple: A tuple containing the dictionary.
        """
        return ({key:value},)
    