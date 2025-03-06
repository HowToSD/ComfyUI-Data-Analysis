from typing import Any, Dict
from datetime import datetime

class PyStringToDatetime:
    """
    Converts a Python string to a Python datetime.datetime.

    Refer to [the Python documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) for date/time format strings.

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
                "value": ("STRING", {"default":"", "multiline": False}),
                "date_format": ("STRING", {"default":"%Y-%m-%d %H:%M:%S", "multiline": False}),
            }
        }

    RETURN_TYPES: tuple = ("PYDATETIME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, value: str, date_format: str) -> tuple:
        """
        Converts a Python string to Python datetime.datetime.
        
        Args:
            value (str): String value to convert.

        Returns:
            tuple: A tuple containing the dictionary.
        """
        return (datetime.strptime(value, date_format),)
    