from typing import Any, Dict
from io import StringIO
import pandas as pd
from .utils import series_to_jsons

class PandasLocRowSeries:
    """
    PandasLocRowSeries:
        A class for selecting a row from a pandas DataFrame and output as a Series.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `select_row` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe_json": ("STRING", {"multiline": True}),
                "row_index": ("STRING", {"default": ""}),
                "row_index_type":(("string", "int"),)
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "select_row"
    CATEGORY: str = "Data Analysis"

    def select_row(self, dataframe_json: str,
             row_index: str,
             row_index_type: str) -> tuple:
        """
        Selects a specific row using a row label (row index) from a pandas DataFrame,
        and returns the JSON serialized Series object.

        Args:
            dataframe_json (str): A JSON string representation of the DataFrame.
            row_index (str): The row index (row label) for the row.
            row_index_type (str): The data type of the row index.

        Returns:
            tuple: A tuple containing the value of the row in string. The string is
                   a JSON string containing the serialized Pandas Series object.
        """
        # Deserialize JSON string to DataFrame
        df = pd.read_json(StringIO(dataframe_json))
        row_index = int(row_index) if row_index_type == "int" else row_index

        value = df.loc[row_index]
        return (series_to_jsons(value),)
