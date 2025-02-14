from typing import Any, Dict
from io import StringIO
import pandas as pd
from .utils import index_to_jsons

class PandasIndex:
    """
    PandasColumns:
        A class for retrieving the row labels (index) of a pandas DataFrame.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `row_index` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe_json": ("STRING", {"multiline": True})
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "row_index"
    CATEGORY: str = "Data Analysis"

    def row_index(self, dataframe_json: str) -> tuple:
        """
        Returns the row labels (index) of a pandas DataFrame.

        Args:
            dataframe_json (str): A JSON string representation of the DataFrame.

        Returns:
            tuple: A tuple containing a JSON string for the serialized pandas.Index containing row labels.
        """
        # Deserialize JSON string to DataFrame
        df = pd.read_json(StringIO(dataframe_json))
        row_index = df.index
        return (index_to_jsons(row_index),)
