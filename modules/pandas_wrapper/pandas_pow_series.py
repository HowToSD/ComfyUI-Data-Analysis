from typing import Any, Dict
from io import StringIO
import pandas as pd
from .utils import jsons_to_series

class PandasPowSeries:
    """
    PandasPowSeries:
        A class for raising a Pandas DataFrame to the power of a Pandas Series.
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
        Raise a pandas DataFrame to the power of a pandas Series.

        Args:
            a_dataframe (DataFrame): The base DataFrame.
            b_series (Series): The exponent Series.

        Returns:
            tuple: A tuple containing the DataFrame containing the result of exponentiation.
        """
        df_out = a_dataframe.pow(b_series)
        return (df_out,)
