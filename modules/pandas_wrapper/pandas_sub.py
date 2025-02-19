from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasSub:
    """
    Subtracts a Pandas DataFrame from another DataFrame.

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
        Subtracts a Pandas DataFrame from another DataFrame.

        Args:
            a_dataframe (DataFrame): The left DataFrame.
            b_dataframe (DataFrame): The right DataFrame.

        Returns:
            tuple: A tuple containing the DataFrame containing the result of subtraction.
        """
        df_out = a_dataframe.sub(b_dataframe)
        return (df_out,)
