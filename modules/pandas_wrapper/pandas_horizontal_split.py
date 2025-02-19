from typing import Any, Dict
import pandas as pd


class PandasHorizontalSplit:
    """
    Horizontally splits a Pandas DataFrame into two pandas DataFrames.

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
                "column_integer_position": ("INT", {"default": 0, "min": -1, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME", "DATAFRAME")
    RETURN_NAMES: tuple = ("Left DataFrame", "Right DataFrame")

    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, column_integer_position: int) -> tuple:
        """
        Horizontally splits a Pandas DataFrame into two pandas DataFrames.

        Args:
            dataframe (pd.DataFrame): The DataFrame to split.
            column_integer_position (int): The column integer position where the split occurs. 
                The left DataFrame contains columns [0, column_integer_position-1], 
                and the right DataFrame contains columns [column_integer_position, end].

        Returns:
            tuple: A tuple containing the left and right DataFrames.
        """
        df_left = dataframe.iloc[:,:column_integer_position]
        df_right = dataframe.iloc[:,column_integer_position:]
        
        return (df_left, df_right)
