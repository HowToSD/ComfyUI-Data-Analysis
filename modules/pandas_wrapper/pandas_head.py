from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasHead:
    """
    PandasHead:
        A class for retrieving the first few rows of a pandas DataFrame.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `head` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
                "rows": ("INT", {"default": 10, "min": 0, "max": 50})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "head"
    CATEGORY: str = "Data Analysis"

    def head(self, dataframe: pd.DataFrame, rows: int) -> tuple:
        """
        Returns the first `rows` rows of a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            rows (int): The number of rows to retrieve.

        Returns:
            tuple: A tuple containing a JSON string of the resulting DataFrame.
        """
        df2 = dataframe.head(rows)
        return (df2,)
