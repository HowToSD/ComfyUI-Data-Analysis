from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasGroupBy:
    """
    Computes aggregate values for groups in a DataFrame.

    category: Aggregation
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the function.

        See https://pandas.pydata.org/docs/reference/groupby.html for aggragate functions.
        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
                "column_name": ("STRING", {"default": ""}),
                "aggragate_function":(("sum", "mean", "count", "std", "min", "max"),)
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "groupby_dataframes"
    CATEGORY: str = "Data Analysis"

    def groupby_dataframes(self,
                           dataframe: pd.DataFrame,
                           column_name: str,
                           aggragate_function: str) -> tuple:
        """
        Compute aggregate values for groups in a DataFrame

        Args:
            dataframe (DataFrame): The DataFrame.
            column_name (str): The name of the column for use as groups.
            aggregate_function (str): The type of aggregate function to perform.

        Returns:
            tuple: A tuple containing a JSON string of the merged DataFrame.
        """
        if aggragate_function == "max":
            df_out = dataframe.groupby(column_name).max()
        elif aggragate_function == "min":
            df_out = dataframe.groupby(column_name).min()
        elif aggragate_function == "std":
            df_out = dataframe.groupby(column_name).std()
        elif aggragate_function == "count":
            df_out = dataframe.groupby(column_name).count()
        elif aggragate_function == "sum":
            df_out = dataframe.groupby(column_name).sum()
        elif aggragate_function == "mean":
            df_out = dataframe.groupby(column_name).mean()
        else:
            raise ValueError("Unsupported aggregate function.")
        return (df_out,)
