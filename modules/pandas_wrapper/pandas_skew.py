from typing import Any, Dict
import pandas as pd


class PandasSkew:
    """
    Computes the unbiased skewness of the DataFrame.

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
                "axis": (("index", "columns"),),
            }
        }

    RETURN_TYPES: tuple = ("PDSERIES",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, axis: str) -> tuple:
        """
        Computes the unbiased skewness of the DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            axis (str): Specify the direction to compute: Index (row label) or column label.

        Returns:
            tuple: A tuple containing the series.
        """
        if axis=="index":
            series = dataframe.skew(axis=0)
        elif axis=="columns":
            series = dataframe.skew(axis=1)
        else:
            raise ValueError("Invalid axis. Only index or columns are supported.")
        return (series,)
