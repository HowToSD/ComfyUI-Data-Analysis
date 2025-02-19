from typing import Any, Dict
from io import StringIO
import pandas as pd

class PandasSelectRows:
    """
    Selects specific rows from a pandas DataFrame based on a condition.

    category: Data subset selection
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `select_rows` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
                "condition": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "select_rows"
    CATEGORY: str = "Data Analysis"

    def select_rows(self, dataframe: pd.DataFrame, condition: str) -> tuple:
        """
        Selects specific rows from a pandas DataFrame based on a given condition.

        Args:
            dataframe (DataFrame): The DataFrame.
            condition (str): A string representing the condition to filter rows.

        Returns:
            tuple: A tuple containing a JSON string of the filtered DataFrame.
        """
        # Apply condition
        df2 = dataframe.query(condition)
        return (df2,)
