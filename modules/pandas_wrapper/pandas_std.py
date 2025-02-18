from typing import Any, Dict
from io import StringIO
import pandas as pd
from .utils import series_to_jsons

class PandasStd:
    """
    PandasStd:
        A class for computing the standard deviation of a pandas DataFrame.
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

    RETURN_TYPES: tuple = ("PDSERIES",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame) -> tuple:
        """
        Returns a Series with standard deviation for each column.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing the Series.
        """
        return (dataframe.std(),)
