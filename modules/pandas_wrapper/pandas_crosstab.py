from typing import Any, Dict
import pandas as pd
from .utils import column_labels_string_to_list


class PandasCrosstab:
    """
    Creates a contingency table (crosstab, or cross-tabulation) from two or more columns in a DataFrame.

    category: Categorical summary
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
                "index": ("STRING", {"default": ""}),
                "column_names": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, index: str, column_names: str) -> tuple:
        """
        Creates a contingency table (crosstab, or cross-tabulation) from two or more columns in a DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            index (str): A comma-separated list of index (row labels) containing categorical data.
            column_names (str): A comma-separated list of column names containing categorical data.

        Returns:
            tuple: A tuple containing the DataFrame.
        """
        rows = column_labels_string_to_list(dataframe, index)
        cols = column_labels_string_to_list(dataframe, column_names)

        if len(rows) == 1:
            rows = dataframe[rows[0]]
        else:
            rows = [dataframe[e] for e in rows]
        if len(cols) == 1:
            cols = dataframe[cols[0]]
        else:
            cols = [dataframe[e] for e in cols]
        df2 = pd.crosstab(index=rows, columns=cols)
        return (df2,)
