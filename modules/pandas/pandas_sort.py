from typing import Any, Dict
import pandas as pd

class PandasSort:
    """
    PandasSort:
        A class for sorting a pandas DataFrame by a specified column.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `sort_rows` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe_json": ("STRING", {"multiline": True}),
                "column_name": ("STRING", {"default": ""}),
                "ascending": ("BOOLEAN", {"default": True})
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "sort_rows"
    CATEGORY: str = "Data Analysis"

    def sort_rows(self, dataframe_json: str, column_name: str, ascending: bool) -> tuple:
        """
        Sorts a pandas DataFrame by the specified column.

        Args:
            dataframe_json (str): A JSON string representation of the DataFrame.
            column_name (str): The name of the column to sort by.
            ascending (bool): Whether to sort in ascending order.

        Returns:
            tuple: A tuple containing a JSON string of the sorted DataFrame.
        """
        # Deserialize JSON string to DataFrame
        df = pd.read_json(dataframe_json)
        
        # Sort DataFrame
        df2 = df.sort_values(by=column_name, ascending=ascending)
        
        return (df2.to_json(),)
