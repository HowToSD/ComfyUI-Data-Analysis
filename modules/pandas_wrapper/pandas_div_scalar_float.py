from typing import Any, Dict
import pandas as pd


class PandasDivScalarFloat:
    """
    Divides a Pandas DataFrame by a floating-point number.

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
                "float_scalar": ("FLOAT", {"default": 1.0, "min": -2**31, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, float_scalar: float) -> tuple:
        """
        Divides a Pandas DataFrame by a floating-point number.

        Args:
            dataframe (DataFrame): The DataFrame to be divided.
            float_scalar (DataFrame): The scalar value to divide by.

        Returns:
            tuple: A tuple containing the DataFrame containing the result of division.
        """
        df_out = dataframe / float_scalar
        return (df_out,)
