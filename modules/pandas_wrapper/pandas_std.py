from typing import Any, Dict
from io import StringIO
import pandas as pd
from .utils import series_to_jsons

class PandasStd:
    """
    PandasStd:
        A class for computing the standard deviation of a pandas DataFrame.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe_json": ("STRING", {"multiline": True})
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe_json: str) -> tuple:
        """
        Returns a Series with standard deviation for each column.

        Args:
            dataframe_json (str): A JSON string representation of the DataFrame.

        Returns:
            tuple: A tuple containing a JSON string for the Series.
        """
        # Deserialize JSON string to DataFrame
        df = pd.read_json(StringIO(dataframe_json))
        return (series_to_jsons(df.std()),)
