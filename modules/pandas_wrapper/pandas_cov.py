from typing import Any, Dict
import pandas as pd


class PandasCov:
    """
    Computes the covariance of the DataFrame.

    category: Summary statistics
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
        Computes the covariance of the DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing the result.
        """
        return (dataframe.cov(),)
