from typing import Any, Dict
import pandas as pd


class PandasIsNA:
    """
    Pandas Is NA:
    Checks a pandas DataFrame for missing values.

    category: Data cleansing
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
    FUNCTION: str = "isna"
    CATEGORY: str = "Data Analysis"

    def isna(self, dataframe: pd.DataFrame) -> tuple:
        """
        Returns a DataFrame with boolean values with True indicating a missing value.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing the DataFrame.
        """
        return (dataframe.isna(),)
