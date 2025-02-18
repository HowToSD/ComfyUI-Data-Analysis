from typing import Any, Dict
import pandas as pd


class PandasColumns:
    """
    PandasColumns:
        A class for retrieving the column labels of a pandas DataFrame.
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `columns` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {})
            }
        }

    RETURN_TYPES: tuple = ("PDINDEX",)
    FUNCTION: str = "columns"
    CATEGORY: str = "Data Analysis"

    def columns(self, dataframe: pd.DataFrame) -> tuple:
        """
        Returns the column labels of a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing a pandas.Index for columns.
        """
        columns = dataframe.columns
        return (columns,)
