from typing import Any, Dict
import pandas as pd


class PandasReplace:
    """
    Replaces part or all of a string in each DataFrame cell with a specified string using a wildcard for matching.  If you want to remove some characters, then leave the replace_string field blank.

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
                "regex": ("STRING", {"default": ""}),
                "replacement_string": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, regex: str, replacement_string: str) -> tuple:
        """
        Replaces part or all of a string in each DataFrame cell with a specified string using a wildcard for matching.

        Args:
            dataframe (DataFrame): The target DataFrame.
            regex (str): A regular expression pattern.

        Returns:
            tuple: A tuple containing the DataFrame.
        """
        df2 = dataframe.replace({regex: replacement_string}, regex=True)
        return (df2,)
