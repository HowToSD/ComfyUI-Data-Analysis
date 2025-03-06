from typing import Any, Dict
import pandas as pd


class PandasIatSetFloat:
    """
    Sets a Python float data in a cell from a pandas DataFrame.

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
                "data": ("FLOAT", {"default": 0, "min": -2**63, "max": 2**63, "step": 0.00000001})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame,
             row_integer_position: int,
             column_integer_position: int,
             data: float) -> tuple:
        """
        Sets a Python float data in a cell in a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            row_integer_position (int): The row integer position for the cell.
            column_integer_position (int): The row integer position for the cell.
            data (float): The value to set in the cell.
             
        Returns:
            tuple: A tuple containing the updated DataFrame.
        """
        dataframe.iat[row_integer_position, column_integer_position] = data
        return (dataframe,)
