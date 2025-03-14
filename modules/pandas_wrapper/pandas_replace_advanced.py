from typing import Any, Dict
import pandas as pd
import ast

class PandasReplaceAdvanced:
    """
    Replaces strings in a DataFrame cell using a mapping specified in a dictionary.
    For example, if you want to replace "cat" with "dog" and replace "mountain" with "ocean", specify the mapping in Python dict format:
    ```
    {"cat":"dog", "mountain":"ocean"}
    ```
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
                "replacement_dict": ("STRING", {"default": "{}", "multiline":True})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, replacement_dict: str) -> tuple:
        """
        Replaces part or all of a string in each DataFrame cell with a specified string using a wildcard for matching.

        Args:
            dataframe (DataFrame): The target DataFrame.
            replacement_dict (str): A dict containing the mapping.

        Returns:
            tuple: A tuple containing the DataFrame.
        """
        d = ast.literal_eval(replacement_dict)
        if isinstance(d, dict) is False:
            raise ValueError('You need to specify the mapping in Python dict format such as {"cat":"dog", "mountain":"ocean"}')
        # check values
        for k, v in d.items():
            if (isinstance(k, str) is False and 
                isinstance(k, float) is False and
                isinstance(k, int) is False):
                raise ValueError("You need to specify a string or a number for source values.")

            if (isinstance(v, str) is False and 
                isinstance(v, float) is False and
                isinstance(v, int) is False):
                raise ValueError("You need to specify a string or a number for target values.")

        df2 = dataframe.replace(to_replace=d)
        return (df2,)
