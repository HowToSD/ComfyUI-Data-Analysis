from typing import Any, Dict
import pandas as pd
from .utils import column_labels_string_to_list

class PandasSelectColumnAsSeries:
    """
    Selects specific column as Series from a pandas DataFrame.

    category: Data subset selection
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
                "dataframe": ("DATAFRAME", {}),
                "column_name": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES: tuple = ("PDSERIES",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, column_name: str) -> tuple:
        """
        Selects specific column as Series from a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            column_name (str): A column name to select.

        Returns:
            tuple: A tuple containing the Series with selected column.
        """
        series = dataframe[column_name]
        return (series,)
