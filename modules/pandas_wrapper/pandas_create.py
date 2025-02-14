from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasCreate:
    """
    PandasLoadCSV:
        A class for creating a pandas DataFrame using values entered in the text field.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `create` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "data": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "create"
    CATEGORY: str = "Data Analysis"

    def create(self, data: str) -> tuple:
        """
        Create a pandas DataFrame using values entered in the text field and converts it to a JSON string.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            tuple: A tuple containing a JSON string representation of the DataFrame.
        """
        # Read CSV file into DataFrame
        df = pd.read_csv(StringIO(data))

        # Convert DataFrame to JSON
        result_json = df.to_json()

        return (result_json,)
