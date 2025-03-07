from typing import Any, Dict
import pandas as pd


class PandasGe:
    """
    Determines whether each element in the first pandas DataFrame is greater than or equal to the corresponding element in the second DataFrame.

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
                "a_dataframe": ("DATAFRAME", {}),
                "b_dataframe": ("DATAFRAME", {})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, a_dataframe: pd.DataFrame, b_dataframe: pd.DataFrame) -> tuple:
        """
        Determines whether each element in the first pandas DataFrame is greater than or equal to the corresponding element in the second DataFrame.

        Args:
            a_dataframe (DataFrame): The left DataFrame.
            b_dataframe (DataFrame): The right DataFrame.

        Returns:
            tuple: A tuple containing the DataFrame containing the result of operation.
        """
        df_out = a_dataframe.ge(b_dataframe)
        return (df_out,)
