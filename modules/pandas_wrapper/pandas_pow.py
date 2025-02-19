from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasPow:
    """
    Exponentiates two pandas DataFrames.

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
                # "a_dataframe": ("DATAFRAME", {}),
                # "b_dataframe": ("DATAFRAME", {})
                "a_dataframe": ("DATAFRAME", {}),
                "b_dataframe": ("DATAFRAME", {})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    # def f(self, a_dataframe: pd.DataFrame, b_dataframe: pd.DataFrame) -> tuple:
    def f(self, a_dataframe: pd.DataFrame, b_dataframe: pd.DataFrame) -> tuple:
        """
        Raise one pandas DataFrame to the power of another.

        Args:
            a_dataframe (DataFrame): The base DataFrame.
            b_dataframe (DataFrame): The exponent DataFrame.

        Returns:
            tuple: A tuple containing the DataFrame containing the result of exponentiation.
        """
        df_out = a_dataframe.pow(b_dataframe)
        return (df_out,)
