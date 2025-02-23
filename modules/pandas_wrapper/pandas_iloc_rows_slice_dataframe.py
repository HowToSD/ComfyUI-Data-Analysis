from typing import Any, Dict
import pandas as pd


class PandasIlocRowsSliceDataFrame:
    """
    Selects rows from a pandas DataFrame using a slice defined by a start and end integer position. The start position is inclusive, while the end position is exclusive. Returns the selected rows as a DataFrame.

    category: Data subset selection
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
                "start_row": ("INT", {"default": 0, "min": -1, "max": 2**31}),
                "end_row": ("INT", {"default": 0, "min": -1, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame,
             start_row: int,
             end_row:int) -> tuple:
        """
        Selects rows from a pandas DataFrame using a slice defined by a start and end integer position. The start position is inclusive, while the end position is exclusive. Returns the selected rows as a DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            start_row (int): The integer position of the start row (inclusive).
            end_row (int): The integer position of the end row (exclusive).

        Returns:
            tuple: A tuple containing the DataFrame.
        """
        df2 = dataframe.iloc[start_row:end_row]
        return (df2,)
