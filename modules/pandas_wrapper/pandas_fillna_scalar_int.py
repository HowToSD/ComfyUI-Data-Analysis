from typing import Any, Dict
import pandas as pd


class PandasFillNAScalarInt:
    """
    Pandas Fill NA Scalar Int:
    Replaces missing values in a Pandas DataFrame with an integer.

    category: Data cleansing
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
                "int_scalar": ("INT", {"default": 0, "min": -2**31, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, int_scalar: int) -> tuple:
        """
        Replaces missing values in a Pandas DataFrame with an integer.

        Args:
            dataframe (DataFrame): The DataFrame.
            int_scalar (DataFrame): The scalar value to replace with.

        Returns:
            tuple: A tuple containing the DataFrame containing the result.
        """
        df_out = dataframe.fillna(int_scalar)
        return (df_out,)
