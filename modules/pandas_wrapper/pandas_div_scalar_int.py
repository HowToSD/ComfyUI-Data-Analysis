from typing import Any, Dict
import pandas as pd


class PandasDivScalarInt:
    """
    Divides a Pandas DataFrame by an integer.

    category: Arithmetic method
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
                "int_scalar": ("INT", {"default": 1, "min": -2**31, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, int_scalar: int) -> tuple:
        """
        Divides a Pandas DataFrame by an integer.

        Args:
            dataframe (DataFrame): The DataFrame to be divided.
            int_scalar (DataFrame): The scalar value to divide by.

        Returns:
            tuple: A tuple containing the DataFrame containing the result of division.
        """
        df_out = dataframe / int_scalar
        return (df_out,)
