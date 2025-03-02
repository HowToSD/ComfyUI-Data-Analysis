from typing import Any, Dict
import pandas as pd


class PandasHorizontalConcat:
    """
    Horizontally concatenates two pandas DataFrames.
    
    If reset labels is set to True, column labels are reset to a sequential integer index.

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
                "b_dataframe": ("DATAFRAME", {}),
                "reset_labels": ("BOOLEAN", {"default": False})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self,
          a_dataframe: pd.DataFrame,
          b_dataframe: pd.DataFrame,
          reset_labels: bool) -> tuple:
        """
        Horizontally concatenate two pandas DataFrames.

        Args:
            a_dataframe (DataFrame): The first DataFrame.
            b_dataframe (DataFrame): The second DataFrame.
            reset_labels (bool): If reset labels is set to True, column labels are reset to a sequential integer index.

        Returns:
            tuple: A tuple containing the concatenated DataFrame.
        """
        df_out = pd.concat([a_dataframe, b_dataframe], axis=1)
        if reset_labels:
            df_out.columns = range(df_out.shape[1])

        return (df_out,)
