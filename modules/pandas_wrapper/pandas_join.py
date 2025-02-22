from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasJoin:
    """
    Merges two pandas DataFrames based on a common column.

    category: Transformation
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `join` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "left_dataframe": ("DATAFRAME", {}),
                "right_dataframe": ("DATAFRAME", {}),
                "on_column_name": ("STRING", {"default": ""}),
                "join_method":(("inner", "left", "right", "outer"),)
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "join_dataframes"
    CATEGORY: str = "Data Analysis"

    def join_dataframes(self, left_dataframe: pd.DataFrame, right_dataframe: pd.DataFrame, on_column_name: str, join_method: str) -> tuple:
        """
        Merges two pandas DataFrames based on a common column using the specified join method.

        Args:
            left_dataframe (DataFrame): The left DataFrame.
            right_dataframe (DataFrame): The right DataFrame.
            on_column_name (str): The name of the column to join on.
            join_method (str): The type of join to perform ("inner", "left", "right", "outer").

        Returns:
            tuple: A tuple containing the merged DataFrame.
        """
        df_out = pd.merge(left_dataframe, right_dataframe, on=on_column_name, how=join_method)
        return (df_out,)
