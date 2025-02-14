from typing import Any, Dict
from io import StringIO
import pandas as pd

class PandasSelectColumns:
    """
    PandasSelectColumns:
        A class for selecting specific columns from a pandas DataFrame.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `select_columns` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe_json": ("STRING", {"multiline": True}),
                "column_names": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "select_columns"
    CATEGORY: str = "Data Analysis"

    def select_columns(self, dataframe_json: str, column_names: str) -> tuple:
        """
        Selects specific columns from a pandas DataFrame.

        Args:
            dataframe_json (str): A JSON string representation of the DataFrame.
            column_names (str): A comma-separated string of column names to select.

        Returns:
            tuple: A tuple containing a JSON string of the DataFrame with selected columns.
        """
        # Deserialize JSON string to DataFrame
        df = pd.read_json(StringIO(dataframe_json))

        # Process column names
        selected_columns = [col.strip() for col in column_names.split(",")]
        df2 = df[selected_columns]
        
        return (df2.to_json(),)
