from typing import Any, Dict
import pandas as pd


class PandasVerticalSplit:
    """
    Vertically splits a Pandas DataFrame into two pandas DataFrames.

    category: Transformation
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
                "row_integer_position": ("INT", {"default": 0, "min": -1, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME", "DATAFRAME")
    RETURN_NAMES: tuple = ("Top DataFrame", "Bottom DataFrame")

    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, row_integer_position: int) -> tuple:
        """
        Vertically splits a Pandas DataFrame into two pandas DataFrames.

        Args:
            dataframe (pd.DataFrame): The DataFrame to split.
            row_integer_position (int): The row integer position where the split occurs. 
                The top DataFrame contains rows [0, row_integer_position-1], 
                and the bottom DataFrame contains rows [row_integer_position, end].

        Returns:
            tuple: A tuple containing the top and bottom DataFrames.
        """
        df_top = dataframe.iloc[:row_integer_position]
        df_bottom = dataframe.iloc[row_integer_position:]
        
        return (df_top, df_bottom)
