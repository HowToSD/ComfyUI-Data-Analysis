from typing import Any, Dict
from io import StringIO
import pandas as pd
from .utils import jsons_to_series

class PandasSeriesToString:
    """
    Converts a pandas Series to a string representation.

    category: Display data
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
                "series": ("PDSERIES", {}),
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "series_to_string"
    CATEGORY: str = "Data Analysis"

    def series_to_string(self, series: pd.Series) -> tuple:
        """
        Converts a Pandas Series to a string representation.

        Args:
            series (Series): The Series.

        Returns:
            tuple: A tuple containing the string representation of the Series.
        """
        return (str(series),)
