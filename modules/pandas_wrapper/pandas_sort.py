from typing import Any, Dict
from io import StringIO
import pandas as pd

class PandasSort:
    """
    PandasSort:
        A class for sorting a pandas DataFrame by a specified column.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `sort_rows` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
                "column_name": ("STRING", {"default": ""}),
                "ascending": ("BOOLEAN", {"default": True})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "sort_rows"
    CATEGORY: str = "Data Analysis"

    def sort_rows(self, dataframe: pd.DataFrame, column_name: str, ascending: bool) -> tuple:
        """
        Sorts a pandas DataFrame by the specified column.

        Args:
            dataframe (DataFrame): The DataFrame.
            column_name (str): The name of the column to sort by.
            ascending (bool): Whether to sort in ascending order.

        Returns:
            tuple: A tuple containing a JSON string of the sorted DataFrame.
        """
        df2 = dataframe.sort_values(by=column_name, ascending=ascending)
        return (df2,)
