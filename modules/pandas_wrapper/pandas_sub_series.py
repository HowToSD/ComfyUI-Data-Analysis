from typing import Any, Dict
from io import StringIO
import pandas as pd
from .utils import jsons_to_series

class PandasSubSeries:
    """
    Subtracts a Pandas Series from a Pandas DataFrame.

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
                "b_series": ("PDSERIES", {})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, a_dataframe: pd.DataFrame, b_series: pd.Series) -> tuple:
        """
        Subtract a pandas Series from a pandas DataFrame.

        Args:
            a_dataframe (DataFrame): The DataFrame.
            b_series (Series): The Series.

        Returns:
            tuple: A tuple containing the DataFrame containing the result of subtraction.
        """
        df_out = a_dataframe.sub(b_series)
        return (df_out,)
