from typing import Any, Dict
from io import StringIO
import pandas as pd

class PandasIatInt:
    """
    Selects a cell from a pandas DataFrame and output as a Python int.

    category: Data subset selection
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `cell` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
                "row_integer_position": ("INT", {"default": 0, "min": 0, "max": 2**31}),
                "column_integer_position": ("INT", {"default": 0, "min": 0, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("INT",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame,
             row_integer_position: int,
             column_integer_position: int) -> tuple:
        """
        Selects specific cell from a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            row_integer_position (int): The row integer position for the cell.
            column_integer_position (int): The row integer position for the cell.
             
        Returns:
            tuple: A tuple containing the value of the cell.
        """
        value = dataframe.iat[row_integer_position, column_integer_position]
        return (int(value),)
