from typing import Any, Dict
from io import StringIO
import pandas as pd
from .utils import jsons_to_series

class PandasSeriesToString:
    """
    PandasSeriesToString:
        A class for converting a pandas Series to a string representation.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `to_string` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "series_json": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "series_to_string"
    CATEGORY: str = "Data Analysis"

    def series_to_string(self, series_json: str) -> tuple:
        """
        Converts a Pandas Series to a string representation.

        Args:
            series_json (str): A JSON string representation of the Series.

        Returns:
            tuple: A tuple containing the string representation of the Series.
        """
        # Deserialize JSON string to DataFrame
        series = jsons_to_series(series_json)
        return (str(series),)
