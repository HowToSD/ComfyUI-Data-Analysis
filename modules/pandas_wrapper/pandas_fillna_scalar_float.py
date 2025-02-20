from typing import Any, Dict
import pandas as pd


class PandasFillNAScalarFloat:
    """
    Pandas Fill NA Scalar Float:
    Replaces missing values in a Pandas DataFrame with a floating-point number.

    To set the value, use **the CDA Float Create node** to define the floating-point number and connect it to this node's float_scaler input. Alternatively, you can enter the value directly in this node, but it currently supports only one decimal digit.

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
                "float_scalar": ("FLOAT", {"default": 0.0, "min": -2**31, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, float_scalar: float) -> tuple:
        """
        Replaces missing values in a Pandas DataFrame with a floating-point number.

        Args:
            dataframe (DataFrame): The DataFrame.
            float_scalar (DataFrame): The scalar value to replace with.

        Returns:
            tuple: A tuple containing the DataFrame containing the result.
        """
        df_out = dataframe.fillna(float_scalar)
        return (df_out,)
