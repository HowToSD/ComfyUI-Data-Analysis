from typing import Any, Dict
from io import StringIO
import pandas as pd

class PandasSelectColumns:
    """
    PandasSelectColumns:
        A class for selecting specific columns from a pandas DataFrame.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `select_columns` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
                "column_names": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "select_columns"
    CATEGORY: str = "Data Analysis"

    def select_columns(self, dataframe: pd.DataFrame, column_names: str) -> tuple:
        """
        Selects specific columns from a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            column_names (str): A comma-separated string of column names to select.

        Returns:
            tuple: A tuple containing the DataFrame with selected columns.
        """
        selected_columns = [col.strip() for col in column_names.split(",")]
        df2 = dataframe[selected_columns]
        return (df2,)
