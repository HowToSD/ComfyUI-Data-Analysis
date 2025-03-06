from typing import Any, Dict
from datetime import datetime

class PyDatetimeToString:
    """
    Converts a Python datetime.datetime value to a Python string

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
                "value": ("PYDATETIME", {}),
                "date_format": ("STRING", {"default":"%Y-%m-%d %H:%M:%S", "multiline": False}),
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, value: datetime, date_format: str) -> tuple:
        """
        Converts a Python datetime.datetime value to a Python string

        Args:
            value (str): String value to convert.

        Returns:
            tuple: A tuple containing the converted value.
        """
        return (datetime.strftime(value, date_format),)
    