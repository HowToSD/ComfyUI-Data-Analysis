from typing import Any, Dict
import pandas as pd


class PandasSubScalarFloat:
    """
    Subtracts a floating-point number from a Pandas DataFrame.

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
                "float_scalar": ("FLOAT", {"default": 0.0, "min": -2**31, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, float_scalar: float) -> tuple:
        """
        Subtracts a floating-point number from a Pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            float_scalar (DataFrame): The scalar value to subtract.

        Returns:
            tuple: A tuple containing the DataFrame containing the result.
        """
        df_out = dataframe - float_scalar
        return (df_out,)
