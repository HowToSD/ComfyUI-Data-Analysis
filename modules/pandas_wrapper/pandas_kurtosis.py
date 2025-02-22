from typing import Any, Dict
import pandas as pd


class PandasKurtosis:
    """
    Computes the unbiased kurtosis of the DataFrame.

    This method returns the excess kurtosis rather than the raw kurtosis. 
    Excess kurtosis is calculated by subtracting 3 from the raw kurtosis, 
    which offsets it relative to the kurtosis of a normal distribution.

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
        Computes the unbiased kurtosis of the DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            axis (str): Specify the direction to compute: Index (row label) or column label.

        Returns:
            tuple: A tuple containing the series.
        """
        if axis=="index":
            series = dataframe.kurtosis(axis=0)
        elif axis=="columns":
            series = dataframe.kurtosis(axis=1)
        else:
            raise ValueError("Invalid axis. Only index or columns are supported.")
        return (series,)
