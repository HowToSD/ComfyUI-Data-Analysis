from typing import Any, Dict
from io import StringIO
import pandas as pd
from .utils import index_to_jsons

class PandasIsNA:
    """
    PandasColumns:
        A class for checking a pandas DataFrame for missing values.
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
    FUNCTION: str = "isna"
    CATEGORY: str = "Data Analysis"

    def isna(self, dataframe_json: str) -> tuple:
        """
        Returns a DataFrame with boolean values with True indicating a missing value.

        Args:
            dataframe_json (str): A JSON string representation of the DataFrame.

        Returns:
            tuple: A tuple containing a JSON string for the DataFrame.
        """
        # Deserialize JSON string to DataFrame
        df = pd.read_json(StringIO(dataframe_json))
        return (df.isna().to_json(),)
