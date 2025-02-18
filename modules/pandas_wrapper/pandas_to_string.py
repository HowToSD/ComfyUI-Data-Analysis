from typing import Any, Dict
from io import StringIO
import pandas as pd

class PandasToString:
    """
    PandasToString:
        A class for converting a pandas DataFrame to a string representation.
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
                "dataframe": ("DATAFRAME", {}),
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "to_string"
    CATEGORY: str = "Data Analysis"

    def to_string(self, dataframe: pd.DataFrame) -> tuple:
        """
        Converts a pandas DataFrame to a string representation.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing the string representation of the DataFrame.
        """
        return (str(dataframe),)
