from typing import Any, Dict
import pandas as pd


class PandasCumprod:
    """
    Computes the cumprod (cumulative product) of the DataFrame.

    category: Cumulative calculations
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

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, axis: str) -> tuple:
        """
        Computes the cumprod (cumulative product) of the DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            axis (str): Specify the direction to compute: Index (row label) or column label.

        Returns:
            tuple: A tuple containing the DataFrame.
        """
        if axis=="index":
            df_out = dataframe.cumprod(axis=0)
        elif axis=="columns":
            df_out = dataframe.cumprod(axis=1)
        else:
            raise ValueError("Invalid axis. Only index or columns are supported.")
        return (df_out,)
