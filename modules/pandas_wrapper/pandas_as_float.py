from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasAsFloat:
    """
    PandasAsFloat:
        A class for converting all cells in a pandas DataFrame to float type.
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
                "dataframe": ("DATAFRAME", {})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame) -> tuple:
        """
        Converts all cells in the DataFrame to float type.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing the DataFrame with all values as floats.
        """
        # Convert all values to float, non-numeric values become NaN
        df = dataframe.apply(pd.to_numeric, errors='coerce').astype(float)
        return (df,)
