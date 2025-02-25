from typing import Any, Dict
import pandas as pd
from .utils import column_labels_string_to_list


class PandasValueCounts:
    """
    Creates a frequency table from one or more columns in a DataFrame.

    ![Frequency table](../images/frequency_table.png)

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
                "column_names": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, column_names: str) -> tuple:
        """
        Creates a frequency tableConverts one or more columns in a DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            column_names (str): A comma-separated list of column names containing categorical data.

        Returns:
            tuple: A tuple containing the DataFrame with selected columns.
        """

        # Note
        # If the original DataFrame contains a single column with categorical variables:
        #
        # Category
        # --------
        # A
        # A
        # A
        # B
        # B
        # C
        # C
        # 
        # and you want to compute the count of each variable and call value_counts().
        # After value_counts(), the column entries are became the index in a generated Series:
        # df["Category"].value_counts().to_frame()
        #           Category
        # A         3
        # B         2
        # C         2
        #
        # After you call reset_index, A, B, C are converted back to a column, but the column label
        # is set to "index".
        # Therefore, you need to do the following:
        # * Convert a Series to a DataFrame (to_frame)
        # * Rename the count column to Count (rename)
        # * Convert the original column from index to a column (reset_index)
        # * Restore the original column label (rename)
        cols = column_labels_string_to_list(dataframe, column_names)
        if len(cols) == 1:
            col_label = cols[0]
            df2 = dataframe[col_label].value_counts().to_frame().rename(columns={col_label:"Count"}).reset_index().rename(columns={"index":col_label})
        else:
            df2 = dataframe[cols].value_counts().to_frame().rename(columns={0:"Count"}).reset_index()
        return (df2,)
