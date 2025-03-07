from typing import Any, Dict
import pandas as pd


class PandasLtScalarInt:
    """
    Determines whether each element in the pandas DataFrame is less than the int.

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
                "number": ("INT", {"default": 0, "min": -2**31, "max": 2**31}
)

            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, number: int) -> tuple:
        """
        Determines whether each element in the pandas DataFrame is less than the int.

        Args:
            dataframe (DataFrame): The DataFrame.
            number (int): The number.

        Returns:
            tuple: A tuple containing the DataFrame containing the result of operation.
        """
        df_out = dataframe.lt(number)
        return (df_out,)
