from typing import Any, Dict
from io import StringIO
import pandas as pd
from .utils import jsons_to_series

class PandasDivSeries:
    """
    PandasDivSeries:
        A class for dividing a Pandas DataFrame by a Pandas Series.
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
        Divide a pandas DataFrame by a pandas Series.

        Args:
            a_dataframe (DataFrame): The numerator DataFrame.
            b_series (Series): The denominator Series.

        Returns:
            tuple: A tuple containing the DataFrame containing the result of division.
        """
        df_out = a_dataframe.div(b_series)
        return (df_out,)
