from typing import Any, Dict
import pandas as pd


class PandasAdd:
    """
    Adds two pandas DataFrames.

    category: Arithmetic method
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
                "a_dataframe": ("DATAFRAME", {}),
                "b_dataframe": ("DATAFRAME", {})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, a_dataframe: pd.DataFrame, b_dataframe: pd.DataFrame) -> tuple:
        """
        Add two pandas DataFrames.

        Args:
            a_dataframe (DataFrame): The left DataFrame.
            b_dataframe (DataFrame): The right DataFrame.
            on_column_name (str): The name of the column to join on.
            join_method (str): The type of join to perform ("inner", "left", "right", "outer").

        Returns:
            tuple: A tuple containing the DataFrame containing the result of addition.
        """
        df_out = a_dataframe.add(b_dataframe)
        return (df_out,)
