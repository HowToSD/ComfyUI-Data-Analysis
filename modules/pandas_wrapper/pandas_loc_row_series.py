from typing import Any, Dict
from io import StringIO
import pandas as pd
from .utils import series_to_jsons

class PandasLocRowSeries:
    """
    Selects a row from a pandas DataFrame and output as a Series.

    category: Data subset selection
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
                "dataframe": ("DATAFRAME", {}),
                "row_index": ("STRING", {"default": ""}),
                "row_index_type":(("string", "int"),)
            }
        }

    RETURN_TYPES: tuple = ("PDSERIES",)
    FUNCTION: str = "select_row"
    CATEGORY: str = "Data Analysis"

    def select_row(self, dataframe: pd.DataFrame,
             row_index: str,
             row_index_type: str) -> tuple:
        """
        Selects a specific row using a row label (row index) from a pandas DataFrame,
        and returns the Series object.

        Args:
            dataframe (DataFrame): The DataFrame.
            row_index (str): The row index (row label) for the row.
            row_index_type (str): The data type of the row index.

        Returns:
            tuple: A tuple containing the value of the row in the serialized Pandas Series object.
        """
        row_index = int(row_index) if row_index_type == "int" else row_index
        value = dataframe.loc[row_index]
        return (value,)
