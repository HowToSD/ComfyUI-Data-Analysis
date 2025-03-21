from typing import Any, Dict
import pandas as pd


class PandasVerticalConcat:
    """
    Vertically concatenates two pandas DataFrames.

    category: Transformation
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
        Vertically concatenate two pandas DataFrames.

        Args:
            a_dataframe (DataFrame): The first DataFrame.
            b_dataframe (DataFrame): The second DataFrame.

        Returns:
            tuple: A tuple containing the concatenated DataFrame.
        """
        df_out = pd.concat([a_dataframe, b_dataframe], axis=0, ignore_index=True)
        return (df_out,)
