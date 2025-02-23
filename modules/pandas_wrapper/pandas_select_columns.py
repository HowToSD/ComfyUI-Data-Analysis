from typing import Any, Dict
import pandas as pd
from .utils import column_labels_string_to_list

class PandasSelectColumns:
    """
    Selects specific columns from a pandas DataFrame.

    category: Data subset selection
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `select_columns` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
                "column_names": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, column_names: str) -> tuple:
        """
        Selects specific columns from a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            column_names (str): A comma-separated string of column names to select.

        Returns:
            tuple: A tuple containing the DataFrame with selected columns.
        """
        selected_columns = column_labels_string_to_list(dataframe, column_names)
        df2 = dataframe[selected_columns]
        return (df2,)
