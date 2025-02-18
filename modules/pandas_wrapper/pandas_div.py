from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasDiv:
    """
    PandasDiv:
        A class for dividing two pandas DataFrames.
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
        Divide two pandas DataFrames.

        Args:
            a_dataframe (DataFrame): The left DataFrame.
            b_dataframe (DataFrame): The right DataFrame.

        Returns:
            tuple: A tuple containing the DataFrame containing the result of division.
        """
        df_out = a_dataframe.div(b_dataframe)
        return (df_out,)
