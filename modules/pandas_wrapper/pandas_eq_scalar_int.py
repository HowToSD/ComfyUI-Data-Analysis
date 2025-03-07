from typing import Any, Dict
import pandas as pd


class PandasEqScalarInt:
    """
    Determines whether each element in the pandas DataFrame is equal to the float.

    category: Logical operations
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
                "number": ("INT", {"default": 0, "min": -2**31, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, number: float) -> tuple:
        """
        Determines whether each element in the pandas DataFrame is equal to the float.

        Args:
            dataframe (DataFrame): The DataFrame.
            number (float): The number.

        Returns:
            tuple: A tuple containing the DataFrame containing the result of operation.
        """
        df_out = dataframe.eq(number)
        return (df_out,)
