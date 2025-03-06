from typing import Any, Dict
import pandas as pd


class PandasIatSetInt:
    """
    Sets a Python int data in a cell from a pandas DataFrame.

    This modifies the input DataFrame in place.
 
    category: Transformation
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
                "column_integer_position": ("INT", {"default": 0, "min": 0, "max": 2**31}),
                "data": ("INT",  {"default": 0, "min": -2**31, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame,
             row_integer_position: int,
             column_integer_position: int,
             data: int) -> tuple:
        """
        Sets a Python int data in a cell in a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            row_integer_position (int): The row integer position for the cell.
            column_integer_position (int): The row integer position for the cell.
            data (int): The value to set in the cell.
             
        Returns:
            tuple: A tuple containing the updated DataFrame.
        """
        dataframe.iat[row_integer_position, column_integer_position] = data
        return (dataframe,)
