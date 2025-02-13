from typing import Any, Dict
import pandas as pd


class PandasJoin:
    """
    PandasJoin:
        A class for merging two pandas DataFrames based on a common column.
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
                "left_dataframe_json": ("STRING", {"multiline": True}),
                "right_dataframe_json": ("STRING", {"multiline": True}),
                "on_column_name": ("STRING", {"default": ""}),
                "join_method":(("inner", "left", "right", "outer"),)
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "join_dataframes"
    CATEGORY: str = "Data Analysis"

    def join_dataframes(self, left_dataframe_json: str, right_dataframe_json: str, on_column_name: str, join_method: str) -> tuple:
        """
        Merges two pandas DataFrames based on a common column using the specified join method.

        Args:
            left_dataframe_json (str): A JSON string representation of the left DataFrame.
            right_dataframe_json (str): A JSON string representation of the right DataFrame.
            on_column_name (str): The name of the column to join on.
            join_method (str): The type of join to perform ("inner", "left", "right", "outer").

        Returns:
            tuple: A tuple containing a JSON string of the merged DataFrame.
        """
        # Deserialize JSON string to DataFrame
        df_left = pd.read_json(left_dataframe_json)
        df_right = pd.read_json(right_dataframe_json)

        df_out = pd.merge(df_left, df_right, on=on_column_name, how=join_method)
        return (df_out.to_json(),)
