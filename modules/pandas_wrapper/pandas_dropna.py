from typing import Any, Dict
import pandas as pd

class PandasDropNA:
    """
    PandasColumns:
        A class for droping missing values from a pandas DataFrame.
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
    FUNCTION: str = "dropna"
    CATEGORY: str = "Data Analysis"

    def dropna(self, dataframe: pd.DataFrame) -> tuple:
        """
        Returns a DataFrame with missing values removed.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing the DataFrame.
        """
        return (dataframe.dropna().to_json(),)
