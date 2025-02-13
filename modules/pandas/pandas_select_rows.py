import ast
from typing import Any, Dict
import pandas as pd

class PandasSelectRows:
    """
    PandasSelectRows:
        A class for selecting specific rows from a pandas DataFrame based on a condition.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `select_rows` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe_json": ("STRING", {"multiline": True}),
                "condition": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "select_rows"
    CATEGORY: str = "Data Analysis"

    def select_rows(self, dataframe_json: str, condition: str) -> tuple:
        """
        Selects specific rows from a pandas DataFrame based on a given condition.

        Args:
            dataframe_json (str): A JSON string representation of the DataFrame.
            condition (str): A string representing the condition to filter rows.

        Returns:
            tuple: A tuple containing a JSON string of the filtered DataFrame.
        """
        # Deserialize JSON string to DataFrame
        df = pd.read_json(dataframe_json)
        
        # Apply condition
        df2 = df.query(condition)
        
        return (df2.to_json(),)
