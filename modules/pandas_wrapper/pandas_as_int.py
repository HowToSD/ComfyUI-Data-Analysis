from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasAsInt:
    """
    Converts all cells in a pandas DataFrame to integer type.

    category: Data type conversion
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
        Converts all cells in the DataFrame to integer type.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing the DataFrame with all values as integers.
        """
        # Convert all values to integer, non-numeric values become NaN
        df = dataframe.apply(pd.to_numeric, errors='coerce').astype('Int64')
        return (df.to_json(),)
