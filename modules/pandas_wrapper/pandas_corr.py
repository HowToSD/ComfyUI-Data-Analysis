from typing import Any, Dict
import pandas as pd


class PandasCorr:
    """
    Computes the correlation of the DataFrame. You can select from the Pearson, Kendall or Spearman methods.

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
                "dataframe": ("DATAFRAME", {}),
                "method": (("pearson", "kendall", "spearman"),)
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, method: str) -> tuple:
        """
        Computes the correlation of the DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing the result.
        """
        return (dataframe.corr(method),)
