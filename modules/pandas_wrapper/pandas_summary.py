from typing import Any, Dict
from io import StringIO
import pandas as pd

class PandasSummary:
    """
    PandasSummary:
        A class for analyzing and summarizing a pandas DataFrame.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `analyze_dataframe` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "analyze_dataframe"
    CATEGORY: str = "Data Analysis"

    def analyze_dataframe(self, dataframe: pd.DataFrame) -> tuple:
        """
        Analyzes a pandas DataFrame and returns a summary.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing a string representation of the DataFrame summary.
        """
        summary = dataframe.describe()
        return (str(summary),)
